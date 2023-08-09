from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('post-list/', views.postList),
    path('post-details/<int:id>/', views.postDetails)
]

