from rest_framework import status
from django.urls import reverse
from home.tests.tests import BlogBaseTest

class BlogPostTests(BlogBaseTest):
    def setUp(self):
        super().setUp()

    def test_create_blog_post_success(self):
        data = {"title": "Test new Blog", "blog_text": "This is a test blog post."}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "blog created successfully")
        self.assertEqual(response.data["data"]["title"], "Test new Blog")
        self.assertEqual(response.data["data"]["blog_text"], "This is a test blog post.")

    def test_create_blog_post_missing_fields(self):
        data = {"title": "Test Blog"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("blog_text", response.data["data"])
        self.assertEqual(response.data["message"], "something went wrong")

    def test_create_blog_post_invalid_data(self):
        data = {"title": "", "blog_text": "This is a test blog post."}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data["data"])
        self.assertEqual(response.data["message"], "something went wrong")

    def test_create_blog_post_unauthenticated(self):
        self.client.logout()
        data = {"title": "Test Blog", "blog_text": "This is a test blog post."}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
