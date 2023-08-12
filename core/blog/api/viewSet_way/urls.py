from django.urls import path, include
from . import api_views
from rest_framework.routers import DefaultRouter

app_name = 'viewSet-way'

router = DefaultRouter()
router.register('post', api_views.PostViewSet, basename='post')

urlpatterns = router.urls
