from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def home(request):
    return render(request,'blog/index.html', {})


def github_api(request):
    # We can also combine Django with APIs. This code does an API request, and
    # then renders the HTML template with the response, every time we visit
    # this view.
    response = requests.get('https://api.github.com/users/camibrennan/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'blog/github_api.html', context)

