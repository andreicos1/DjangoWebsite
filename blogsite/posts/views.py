from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib import messages

from users.models import User
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'posts/posts_index.html'

    def get_queryset(self):
        '''to not show posts with published dates in the future'''
        return Post.objects.filter(pub_date__lte=timezone.now())[:12]


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comment_set.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.commenter = request.user
            new_comment.save()
    else:
        form = CommentForm()
    return render(request,'posts/post_detail.html', {'post':post,
                                                    'comments':comments,
                                                    'new_comment':new_comment,
                                                    'form':form})


@method_decorator(login_required, name = 'dispatch')
class CommentDeleteView(generic.DeleteView):
    model = Comment
    def get_success_url(self):
        next = self.request.POST.get('next', '/')
        return next
