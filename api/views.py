from django.contrib.auth.models import User
from .serializers import ForAdminBookSerializer, ForUserBookSerializer, AuthorSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .models import Book, Author
from .permission import IsOwnerOrDisabled


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDisabled]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ForAdminBookSerializer
        return ForUserBookSerializer

    def perform_create(self, serializer):
        author = Author.objects.get(user=self.request.user)
        if not self.request.user.is_superuser:
            serializer.save(writer=author)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
