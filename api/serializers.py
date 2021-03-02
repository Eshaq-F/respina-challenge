from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Author


class ForAdminBookSerializer(serializers.ModelSerializer):
    writers = Author.objects.all()
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:book-detail')
    writer = serializers.HyperlinkedRelatedField(view_name='api:author-detail', queryset=writers)
    code = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ['url', 'id', 'code', 'title', 'content', 'writer', 'category']
        extra_kwargs = {
            'content': {'write_only': True}
        }


class ForUserBookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:book-detail')
    writer = serializers.HyperlinkedRelatedField(view_name='api:author-detail', read_only=True)
    code = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ['url', 'id', 'code', 'title', 'content', 'writer', 'category']
        extra_kwargs = {
            'content': {'write_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:user-detail')

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name']


class AuthorSerializer(serializers.Serializer):
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api:book-detail')
    user = UserSerializer()

    class Meta:
        model = Author
        fields = ['id', 'user']
