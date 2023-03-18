# from feedback.models import Like, Rating, Comment
# from rest_framework import serializers

# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'

# class RatingSerializer(serializers.ModelSerializer):
#     rating = serializers.IntegerField(min_value=1, max_value=5)

#     class Meta:
#         model = Rating
#         fields = ('rating',)

# class CommentSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.email')
    
#     class Meta:
#         model = Comment
#         fields = '__all__'