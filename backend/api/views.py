from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer, UserFormSubmissionSerializer
from .models import Blog, UserFormSubmission
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

class BlogPostPagination(PageNumberPagination):
    page_size = 12  # Set the number of blog posts per page

class BlogPostListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        blog_posts = Blog.objects.all()
        paginator = BlogPostPagination()
        result_page = paginator.paginate_queryset(blog_posts, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class UserFormSubmissionView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(blog_id=blog_id)
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

class LatestBlogsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        # Fetch the latest 3 blogs based on their `id` (assuming `id` correlates with creation order)
        latest_blogs = Blog.objects.order_by('-blog_id')[:3]
        serializer = BlogSerializer(latest_blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)