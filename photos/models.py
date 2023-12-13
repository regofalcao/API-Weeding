from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(null=True, default=None)
    image = models.URLField()  

    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_photos"
    )

    orders = models.ManyToManyField(
        "users.User", through="photos.PhotoOrder", related_name="photo_orders"
    )

class PhotoOrder(models.Model):
    aproved_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Novo campo

    photo = models.ForeignKey(
        "photos.Photo", on_delete=models.CASCADE, related_name="order_photos"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_photos_order"
    )
