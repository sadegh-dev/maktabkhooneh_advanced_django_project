from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'viewSet-way'

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')

urlpatterns = router.urls
