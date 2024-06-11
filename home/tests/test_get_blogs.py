from unittest.mock import patch
from rest_framework import status

from home.tests.tests import BlogBaseTest
from ..models import Blog


class TestGetBlogView(BlogBaseTest):
    def setUp(self):
        super().setUp()
        self.blog1 = Blog.objects.create(
            user=self.user, title="Test Blog 1", blog_text="Content of blog 1"
        )

    def test_validates_all_blogs_returned_successfully(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
        self.assertEqual(response.data["message"], "Blogs fetched successfully")
    
    @patch('home.views.BlogView.get_blogs')
    def test_validates_all_blogs_returned_successfully(self, mock_get_blogs):
        mock_get_blogs.return_value = [self.blog1]
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data["message"], "Blogs fetched successfully")

    @patch('home.views.BlogView.get_blogs')
    def test_validates_matching_blog(self, mock_get_blogs):
        mock_get_blogs.return_value = [self.blog1]

        response = self.client.get(self.url, {"search": "Blog 1"})
        print("RESPJDIWQHKDV",response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]["title"], "Test Blog 1")

    @patch('home.views.BlogView.get_blogs')
    def test_returns_unauthorized_error(self, mock_get_blogs):
        mock_get_blogs.return_value = []
        self.client.credentials()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch('home.views.BlogView.get_blogs')
    def test_raises_if_data_empty(self, mock_get_blogs):
        mock_get_blogs.return_value = []
        response = self.client.get(self.url, {"search": "Nonexistent"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # import pdb;pdb.set_trace()
