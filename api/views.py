from django.contrib.auth.models import User
from .serializers import BookSerializer, AuthorSerializer, UserSerializer
from rest_framework import viewsets, permissions

from .models import Book, Author


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     if not serializer.writer:
    #         serializer.writer = self.request.user


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]