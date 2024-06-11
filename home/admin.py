from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'blog_text')