from django.shortcuts import render
from django.views.generic import TemplateView

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

