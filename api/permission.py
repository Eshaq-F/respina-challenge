from rest_framework import permissions


class IsOwnerOrDisabled(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.writer.user == request.user
