from rest_framework import serializers
from .models import Blog, UserFormSubmission
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_id', 'author', 'title', 'blog_image', 'content', 'event_date']

class UserFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormSubmission
        fields = "__all__"