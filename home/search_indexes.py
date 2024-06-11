
# search_indexes.py

from haystack import indexes
from .models import Blog

class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    blog_text = indexes.CharField(model_attr='blog_text')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
