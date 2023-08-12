from rest_framework import serializers
from blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    ''' class Serializer for Post-model '''
    class Meta :
        fields = ['id', 'image', 'title', 'content',
                   'status', 'published_date', 'author', 
                   'category', 'created_date', 'updated_date']


