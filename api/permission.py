from rest_framework import permissions


# A permission that access adding book Only for Author users!!!
class IsOwnerOrDisabled(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.writer.user == request.user
