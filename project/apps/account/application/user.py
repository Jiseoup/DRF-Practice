from rest_framework import mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from apps.account import serializers


class User(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.UserSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def list_user(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)
