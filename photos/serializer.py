from rest_framework import serializers
from .models import Photo, PhotoOrder
from users.models import User


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    description = serializers.CharField(max_length=300, required=False)
    image_url = serializers.CharField()  # Troque para CharField para armazenar a URL
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)



class PhotoOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="photo.title", read_only=True)
    aproved_by = serializers.CharField(source="user.email", read_only=True)
    aproved_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: PhotoOrder):
        return obj.photo.title

    def get_bought_by(self, obj: PhotoOrder):
        return obj.user.email

    def create(self, validated_data: dict) -> PhotoOrder:
        return PhotoOrder.objects.create(**validated_data)
