import uuid
from rest_framework import status
from django.contrib.auth.models import User
from home.tests.tests import BlogBaseTest


class BlogDeleteTests(BlogBaseTest):
    def setUp(self):
        super().setUp()
        self.data = {"uid": str(self.blog_uid)}

    def test_delete_blog_successfully(self):
        response = self.client.delete(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "blog deleted")

    def test_delete_blog_invalid_id(self):
        data = {"uid": str(uuid.uuid4())}
        response = self.client.delete(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "invalid id")

    def test_delete_blog_not_authorized(self):
        other_user = User.objects.create_user(username="otheruser", password="otherpassword")
        self.client.force_authenticate(user=other_user)
        response = self.client.delete(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "unauthorized request")
