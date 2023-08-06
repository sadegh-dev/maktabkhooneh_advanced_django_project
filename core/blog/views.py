from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import Category, Post


class HomeView(TemplateView):
    """
    a class for the main page 
    and viewing some content 
    """
    
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'home'
        context['posts'] = Post.objects.all()[:2]
        context['categories'] = Category.objects.all()[:3]
        return context


class RedirectToHomePage(RedirectView):
    """ a class for go to home page """

    pattern_name = 'blog:home'


class PostList(ListView):
    """a class for list of posts"""
    
    #model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        result = Post.objects.all()
        return result

