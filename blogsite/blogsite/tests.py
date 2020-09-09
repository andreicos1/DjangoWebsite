from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from topics.models import Topic
from posts.models import Post
from users.models import User

def create_post(title='SomeTitle', post_text='SomeText', pub_date=timezone.now()):
    return Post.objects.create(title=title, post_text = post_text,
                    pub_date = pub_date)


def create_topic(name='SomeTopic', details='SomeDetails', added_date=timezone.now()):
    return Topic.objects.create(name=name, details=details, added_date=added_date)


def create_user(username='SomeUsername', password='SomePassword', email='some@email.com'):
    return User.objects.create(username=username, password=password, email=email)


class IndexViewTest(TestCase):
    def test_index_page_loaded(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
