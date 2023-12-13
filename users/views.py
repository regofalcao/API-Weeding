from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView

from users.permissions import IsOwnerOrAdmin
from users.serializers import UserSerializer, CustomJWTSerializer
from users.models import User

from django.shortcuts import get_object_or_404, render


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)

        return Response(user_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin, IsAuthenticatedOrReadOnly]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        user_serializer = UserSerializer(user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status.HTTP_200_OK)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
