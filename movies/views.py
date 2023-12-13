from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from movies.permissions import IsOwnerOrEmployee
from movies.serializer import MovieSerializer, MovieOrderSerializer
from movies.models import Movie

from django.shortcuts import get_object_or_404, render


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrEmployee]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        movies_seriliazer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(movies_seriliazer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrEmployee]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movies_seriliazer = MovieSerializer(movie)
        return Response(movies_seriliazer.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movies_seriliazer = MovieOrderSerializer(data=request.data)
        movies_seriliazer.is_valid(raise_exception=True)

        movies_seriliazer.save(movie=movie, user=request.user)

        return Response(movies_seriliazer.data, status.HTTP_201_CREATED)
