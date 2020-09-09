from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Topic
from posts.models import Post
from users.models import User
from blogsite.tests import create_post, create_user, create_topic

# Create your tests here.
class TopicIndex(TestCase):
    def test_with_topics(self):
        topic = create_topic()
        response = self.client.get(reverse('topics:index'))
        self.assertContains(response, topic.name)


class TopicDetail(TestCase):
    def test_valid_topic(self):
        topic = create_topic()
        response = self.client.get(reverse('topics:detail', args=(topic.slug,)))
        self.assertContains(response, topic.details)


class PostsListOfTopic(TestCase):
    def test_no_posts(self):
        topic = create_topic()
        response = self.client.get(reverse('topics:list_of_posts',
                args=(topic.slug,)))
        self.assertContains(response, 'No posts yet in this topic.')

    def test_topic_with_posts(self):
        topic = create_topic()
        some_user = create_user()
        post = create_post()
        response = self.client.get(reverse('topics:list_of_posts',
                args=(topic.slug,)))
        self.assertContains(response, post.title)
