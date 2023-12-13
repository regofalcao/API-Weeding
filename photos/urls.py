from django.urls import path
from .views import PhotoView, PhotoDetailView, PhotoOrderView

urlpatterns = [
    path("photos/", PhotoView.as_view(), name="photo-list"),
    path("photos/<int:photo_id>/", PhotoDetailView.as_view(), name="photo-detail"),
    path("photos/<int:photo_id>/orders/", PhotoOrderView.as_view(), name="photo-order"),
]
