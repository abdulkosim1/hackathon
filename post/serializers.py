from rest_framework import serializers
from .models import Post
# from feedback.serializers import LikeSerializer

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    # likes = LikeSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        # representation['owner'] = instance.author.author_title
        # representation['album'] = instance.album.album_title
        # representation['genre'] = instance.genre.genre_title
        representation['total_likes'] = instance.likes.filter(is_like=True).count()
        # representation['ratings'] = instance.ratings.aggregate(Avg('rating'))
        return representation
    

    class Meta:
        model = Post
        fields = '__all__'