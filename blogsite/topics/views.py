from django.shortcuts import render
from .models import Topic
from django.views import generic

# Create your views here.
class TopicList(generic.ListView):
    model = Topic
    template_name='topics/index.html'

class TopicDetail(generic.DetailView):
    model = Topic

class PostsInTopicDetail(generic.DetailView):
    model = Topic
    template_name = 'topics/posts_in_topic.html'
    context_object_name = 'posts_list'
