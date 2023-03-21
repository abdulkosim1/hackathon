import uuid
from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()

class Order(models.Model):
    ORDER_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),
        ('declined', 'declined')
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    product = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS,
        null=True,
        blank=True
    )
    is_confirm = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=30)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.total_price = self.product.price
        return super().save(*args, **kwargs)
