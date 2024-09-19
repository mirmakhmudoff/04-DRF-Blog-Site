from django.urls import path
from .views import BlogListCreateView, BlogDetailView, BlogCommentListView, CommentCreateView, ProfileListView, ProfileDetailView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view()),
    path('blogs/<int:blog_id>/comments/', BlogCommentListView.as_view()),
    path('comments/', CommentCreateView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailView.as_view()),
]
