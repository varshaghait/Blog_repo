from django.urls import reverse, resolve
from home.tests.tests import BlogBaseTest
from home.views import BlogView

class URLTests(BlogBaseTest):
    def setUp(self):
        super().setUp()

    def test_blog_url_resolves(self):
        """Test that the /blog/ URL resolves to the BlogView"""
        resolver = resolve('/api/home/blog/')
        self.assertEqual(resolver.func.view_class, BlogView)

    def test_blog_url_name_reverse(self):
        """Test that the URL named 'blog' correctly reverses to /blog/"""
        url = reverse('blog')
        self.assertEqual(url, '/api/home/blog/')

    def test_blog_view_response(self):
        """Test that the BlogView returns a 200 response for a GET request"""
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Additional checks can be added here to verify response content if needed

