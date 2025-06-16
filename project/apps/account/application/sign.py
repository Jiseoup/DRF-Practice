from rest_framework import mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView, TokenRefreshView

from apps.account import serializers


class Account(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Account ViewSet.

    Provides user registration and deletion functionality.
    """
    serializer_class = serializers.AccountSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def create_account(self, request: Request, *args, **kwargs) -> Response:
        """Register a new user account."""
        return super().create(request, *args, **kwargs)

    def delete_account(self, request: Request, *args, **kwargs) -> Response:
        """Delete an existing user account by primary key."""
        return super().destroy(request, *args, **kwargs)


class Login(TokenObtainPairView):
    """JWT Login View.

    Authenticates the user using username and password.
    Returns an access token and a refresh token upon successful authentication.
    """
    def post(self, request: Request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            return Response({'message': 'Login successful', **response.data}, status=200)

        return response


class Logout(TokenBlacklistView):
    """JWT Logout View.

    Invalidates the provided refresh token by adding it to the blacklist.
    Prevents the token from being used to generate new access tokens.
    """
    def post(self, request: Request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            return Response({'message': 'Logout successful'}, status=200)

        return response


class Refresh(TokenRefreshView):
    """JWT Refresh View.

    Accepts a valid refresh token and returns new tokens.
    Used to maintain authentication without requiring the user to login again.
    """
    def post(self, request: Request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            return Response({**response.data}, status=200)

        return response
