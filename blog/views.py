from rest_framework import generics, permissions
from .models import Blog, Comment, Profile
from .serializers import BlogSerializer, CommentSerializer, ProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = Blog.objects.all()
        search = self.request.query_params.get('search', None)
        order = self.request.query_params.get('order', 'created_at')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset.order_by(order)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BlogCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
