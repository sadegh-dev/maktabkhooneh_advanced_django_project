from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer) :
    ''' serializer class for Post '''
    
    class Meta:
        model = Post
        fields = [
            'id', 
            'image', 
            'title', 
            'content',
            'status',
            'published_date',
            'author',
            'category',
            'created_date',
            'updated_date'            
        ]
        read_only_fields = ['id', 'image', 'created_date', 'updated_date']


