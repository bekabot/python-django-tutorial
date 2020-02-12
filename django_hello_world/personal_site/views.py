# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from .models import Post


def index(request):
    all_posts = Post.objects.all()
    context = {"posts_list": all_posts}
    return render(request, 'personal_site/index.html', context)


def detail(request, post_title):
    try:
        question = Post.objects.get(title=post_title)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
# return render(request, 'personal_site/post.html', {'question': question})


def like(request, post_id):
    return HttpResponse("You're liking position %s." % post_id)
