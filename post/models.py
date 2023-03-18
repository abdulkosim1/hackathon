from django.db import models
from django.contrib.auth import get_user_model
# from account.models import CustomUser as User


User = get_user_model()

class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'{self.title} -----> {self.owner}'
    

