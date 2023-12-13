from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from photos.permissions import IsOwnerOrEmployee
from photos.serializer import PhotoSerializer, PhotoOrderSerializer
from photos.models import Photo

from django.shortcuts import get_object_or_404, render


class PhotoView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrEmployee]

    def get(self, request: Request) -> Response:
        photos = Photo.objects.all()
        result_page = self.paginate_queryset(photos, request)
        photos_serializer = PhotoSerializer(result_page, many=True)

        return self.get_paginated_response(photos_serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class PhotoDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrEmployee]

    def get(self, request: Request, photo_id: int) -> Response:
        photo = get_object_or_404(Photo, id=photo_id)
        photo_serializer = PhotoSerializer(photo)
        return Response(photo_serializer.data)

    def delete(self, request: Request, photo_id: int) -> Response:
        photo = get_object_or_404(Photo, id=photo_id)
        photo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, photo_id) -> Response:
        photo = get_object_or_404(Photo, id=photo_id)
        photo_serializer = PhotoOrderSerializer(data=request.data)
        photo_serializer.is_valid(raise_exception=True)

        photo_serializer.save(photo=photo, user=request.user)

        return Response(photo_serializer.data, status.HTTP_201_CREATED)
