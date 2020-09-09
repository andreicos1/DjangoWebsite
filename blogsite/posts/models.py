import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse


from topics.models import Topic


User=get_user_model()
# Create your models here.
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default = True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default = True)
    title = models.CharField(max_length = 256, unique = True)
    slug = models.SlugField(unique=True, editable = False)
    post_text = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(null = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.slug,))

    class Meta:
        ordering =['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    text = models.TextField(max_length=1500)
    submited_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering =['submited_on']

    def __str__(self):
        return f"Comment '{self.text[-50:]}' by {self.commenter}"
