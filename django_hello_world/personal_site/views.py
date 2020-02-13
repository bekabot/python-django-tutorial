# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'personal_site/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.all()


# should be moved to generic views as IndexView
def detail(request, post_title):
    post = get_object_or_404(Post, title=post_title)
    return render(request, 'personal_site/post.html', {'post': post})


def like(request, post_title):
    return HttpResponse("You're liking position %s." % post_title)


def add(request):
    # wrap following call to try/except
    title = request.POST['title']
    text = request.POST['text']

    Post.objects.create(title=title, text=text)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('personal_site:index'))
