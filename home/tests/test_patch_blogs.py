from rest_framework import status
from django.contrib.auth.models import User

from home.tests.tests import BlogBaseTest


class BlogPatchTests(BlogBaseTest):

    def setUp(self):
        super().setUp()

    def test_update_blog_successfully(self):
        data = {"uid": self.blog_uid, "title": "Updated Title", "blog_text": "Updated Text"}
        response = self.client.patch(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]["title"], "Updated Title")
        self.assertEqual(response.data["data"]["blog_text"], "Updated Text")

    def test_update_blog_invalid_id(self):
        data = {"uid": "invalid-id", "title": "Updated Title", "blog_text": "Updated Text"}
        response = self.client.patch(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "something went wrong")

    def test_update_blog_not_authorized(self):
        other_user = User.objects.create_user(username="otheruser", password="otherpassword")
        self.client.force_authenticate(user=other_user)
        data = {"uid": self.blog_uid, "title": "Updated Title", "blog_text": "Updated Text"}
        response = self.client.patch(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "not authorized")

    def test_update_blog_invalid_data(self):
        data = {"uid": str(self.blog_uid), "title": "", "blog_text": "Updated Text"}
        response = self.client.patch(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("data", response.data)
        self.assertIn("message", response.data)
