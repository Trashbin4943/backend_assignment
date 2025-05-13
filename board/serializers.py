from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','post','comment','created_at']
        read_only_fields=['id','post','created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields=['id','title','body','created_at','comments']
        read_only_fields=['id','created_at']