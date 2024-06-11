from django.db import models
from django.contrib.auth.models import User

import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to="blogs", blank=True, null=True)

    def __str__(self) -> str:
        return self.title

# class Button:
#     pass
# class NewButton:
#     def click(self)

# def clickbutton(button):
#     button.click()


# class Blogs:
#     def __iter_(self):
#         pass
#     def __next__(self):
#         pass



# for blog in Blogs():
#     print(blog)