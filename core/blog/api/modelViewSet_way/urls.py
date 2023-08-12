from django.urls import path, include
from . import api_views
from rest_framework.routers import DefaultRouter

app_name = 'ModelViewSet-way'

router = DefaultRouter()

router.register('category', api_views.CategoryModelViewSet, basename='post')
router.register('post', api_views.PostModelViewSet, basename='category')

urlpatterns = router.urls
