from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission class to check if the user is the owner of the object.

    This class inherits from `permissions.BasePermission` and overrides the `has_object_permission` method.
    It checks if the `owner` attribute of the object matches the `user` attribute of the request.
    If they match, the method returns `True`, indicating that the user has permission to access the object.
    Otherwise, it returns `False`.
    """

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner of the object.

        Parameters:
        - request (Request): The incoming request object.
        - view (View): The view that is being accessed.
        - obj (Object): The object being accessed.

        Returns:
        - bool: `True` if the user is the owner of the object, `False` otherwise.
        """
        if obj.owner == request.user:
            return True
        return False
