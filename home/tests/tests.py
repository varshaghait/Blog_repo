import uuid
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import Blog
from rest_framework_simplejwt.tokens import RefreshToken

class BlogBaseTest(APITestCase):
    def setUp(self):
        self.url = reverse("blog")
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.client = APIClient()
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        self.blog_uid = uuid.uuid4()
        self.blog = Blog.objects.create(
            user=self.user, title="Original Title", blog_text="Original Text", uid=self.blog_uid
        )
