from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('redirect-to-home/', views.RedirectToHomePage.as_view(), name='redirect-to-home'),
    path('posts/', views.PostList.as_view(), name='posts')
]