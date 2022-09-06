from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def posts_list(request):
    template = 'posts/posts_list.html'
    return render(request, template)


def posts_detail(request):
    template = 'posts/posts_detail.html'
    return render(request, template)
