from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from topics.models import Topic
from posts.models import Post
from users.models import User

from blogsite.tests import create_post, create_user, create_topic
# Create your tests here.
class IndexPage(TestCase):
    def test_no_posts(self):
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts to display')

    def test_with_posts(self):
        create_user()
        create_topic()
        post = create_post()
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)


class DetailPage(TestCase):
    def test_displays_text(self):
        create_user()
        create_topic()
        post = create_post()
        response = self.client.get(reverse('posts:detail',args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
