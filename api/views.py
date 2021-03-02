from django.contrib.auth.models import User
from .serializers import ForAdminBookSerializer, ForUserBookSerializer, AuthorSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .models import Book, Author
from .permission import IsOwnerOrDisabled


# This class render all book API.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDisabled]  # Authentications permissions.

    # Method to set right serializer for different users.
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ForAdminBookSerializer
        return ForUserBookSerializer

    # Set current user as writer just while an author create a book!
    def perform_create(self, serializer):
        if self.request.user:
            author = Author.objects.get(user=self.request.user)
            serializer.save(writer=author)
        else:
            serializer.save()


# The view of all Author API.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]  # Authentications permissions.


# Users API views ; Only Superuser can access to these views.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions,
                          permissions.IsAuthenticated]  # Authentications permissions.
