from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from blog.models import Profile


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user)
