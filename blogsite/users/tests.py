import tempfile
import datetime
import io
from PIL import Image
from os import unlink

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from topics.models import Topic
from posts.models import Post, Comment
from users.models import User
from blogsite.tests import create_post, create_user, create_topic
from .forms import SignUpForm

def create_comment(post, commenter, text='SomeComment', active=True):
    return Comment.objects.create(post=post, commenter=commenter,
                                text=text, active = active)
# Create your tests here.
class UsersList(TestCase):
    def test_multiple_users(self):
        first = create_user()
        second = create_user(username='AnotherUsername')
        response = self.client.get(reverse('users:users_list'))
        self.assertContains(response, first.username)
        self.assertContains(response, second.username)


class UserDetail(TestCase):
    def test_user_profile_shows_comments(self):
        this_user = create_user()
        topic = create_topic()
        post = create_post()
        comment = create_comment(post, this_user)
        response = self.client.get(reverse('users:profile', args=(this_user.pk,)))
        self.assertContains(response, comment.text)

    def test_user_comments_page_no_comments(self):
        this_user = create_user()
        response = self.client.get(reverse('users:comments', args=(this_user.pk,)))
        self.assertEquals(response.status_code, 200)

    def test_user_comments_not_active(self):
        this_user = create_user()
        topic = create_topic()
        post = create_post()
        comment = create_comment(post, this_user, active = False)
        response = self.client.get(reverse('users:comments', args=(this_user.pk,)))
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, 'SomeComment')

    def test_user_active_comments_on_multiple_topic(self):
        this_user = create_user()
        first_topic = create_topic()
        first_post = create_post()
        first_comment = create_comment(first_post, this_user, text='FirstText')
        second_topic = create_topic(name='Something else')
        second_post = create_post(title='Different one')
        second_post.topic = second_topic
        second_comment = create_comment(second_post, this_user, text='SecondText')

        response = self.client.get(reverse('users:comments', args=(this_user.pk,)))
        self.assertContains(response, first_comment.text)
        self.assertContains(response, second_comment.text)

    def test_user_profile_fields(self):
        this_user = create_user()
        this_user.profile.bio = 'SomeBio'
        this_user.profile.location = 'SomeLocation'
        this_user.profile.birth_date = '2006-09-25'
        this_user.profile.save()
        response = self.client.get(reverse('users:profile', args=(this_user.pk,)))
        self.assertContains(response, this_user.profile.bio)
        self.assertContains(response, this_user.profile.location)
        self.assertContains(response, '2006-09-25')

    def test_user_profile_picture(self):
        this_user = create_user()
        image = Image.new('RGB', (100, 100))
        image.save('temp.jpg')
        this_user.profile.image = image
        self.assertIsNotNone(this_user.profile.image)


class SignUp(TestCase):
    def test_sign_up_form(self):
        form_data = {'username':'SomeName', 'email':'some@email.com',
                    'password1':'testpassword', 'password2':'testpassword'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
