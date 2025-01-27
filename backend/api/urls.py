from django.urls import path
from api.views import  BlogPostListAPIView, UserFormSubmissionView, BlogDetailView, LatestBlogsView

urlpatterns = [
    path('blogposts/', BlogPostListAPIView.as_view(), name='blog-list'),
    path("form-submissions/", UserFormSubmissionView.as_view(), name="form-submissions"),
    path('blog/<int:blog_id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('LatestBlogs/', LatestBlogsView.as_view(), name='LatestBlogs-detail'),
]
