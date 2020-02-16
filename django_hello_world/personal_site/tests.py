from django.test import TestCase

from .models import Post


class PostModelTests(TestCase):
    def test_db_counter(self):
        Post.objects.create(title="test_title", text="test_text")
        items_count = Post.objects.count()
        self.assertIs(items_count, 1)
