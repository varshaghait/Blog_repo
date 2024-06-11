# from django.test import TestCase
# from unittest.mock import patch, MagicMock
# from django.contrib.auth.models import User
# from ..models import Blog  # Adjust the import according to your project structure
# from home.views import BlogView  # Adjust the import according to your project structure
# from django.http import HttpRequest
# from django.utils import timezone
# from datetime import timedelta

# class TestGetBlogs(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.blog1 = Blog.objects.create(
#             user=self.user, title="Test Blog 1", blog_text="Content of blog 1", created_at=timezone.now()
#         )
#         self.blog2 = Blog.objects.create(
#             user=self.user, title="Test Blog 2", blog_text="Content of blog 2", created_at=timezone.now()
#         )

#     def test_get_blogs_without_search(self):
#         request = HttpRequest()
#         request.user = self.user
#         blog_view = BlogView()

#         blogs = blog_view.get_blogs(request)
        
#         self.assertEqual(len(blogs), 2)
#         self.assertIn(self.blog1, blogs)
#         self.assertIn(self.blog2, blogs)

#     @patch('blog.views.Blog.objects.filter')
#     def test_get_blogs_with_search(self, mock_filter):
#         mock_filter.return_value = [self.blog1]
        
#         request = HttpRequest()
#         request.user = self.user
#         request.GET['search'] = 'Blog 1'
        
#         blog_view = BlogView()
#         blogs = blog_view.get_blogs(request)
        
#         self.assertEqual(len(blogs), 1)
#         self.assertEqual(blogs[0].title, "Test Blog 1")
#         mock_filter.assert_called_with(user=self.user)

#     @patch('blog.views.Blog.objects.filter')
#     def test_get_blogs_with_search_no_results(self, mock_filter):
#         mock_filter.return_value = []
        
#         request = HttpRequest()
#         request.user = self.user
#         request.GET['search'] = 'Nonexistent Blog'
        
#         blog_view = BlogView()
#         blogs = blog_view.get_blogs(request)
        
#         self.assertEqual(len(blogs), 0)
#         mock_filter.assert_called_with(user=self.user)
