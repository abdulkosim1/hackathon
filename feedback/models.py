from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import CustomUser
from django.db import models
from post.models import Post
from django.contrib.auth import get_user_model
# from post.models import User

User = get_user_model()

class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.owner} liked - {self.post.title}'

# class Rating(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
#     users = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
#     rating = models.SmallIntegerField(
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5)
#         ],
#         blank=True, null=True
#     )

#     def __str__(self) -> str:
#         return f'{self.owner} --> {self.post.title}'

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} --> {self.post.title}'
    
class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favotives')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favotites')

    def __str__(self) -> str:
        return f'{self.owner_id} --- {self.post_id}'