from post.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from feedback.models import Comment, Like, Rating, Favorite
from feedback.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from post.serializers import PostSerializer
from post.models import User
from account.serializers import ProfileSerializer
from feedback.serializers import RatingSerializer, FavoriteSerializer


class AddLike(CreateAPIView): # Post запрос на доваление лайков
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]
    
    def post(self, request, pk, *args, **kwargs):
        user = request.user
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        if not like_obj.is_like:
            status = 'unliked'
        return Response({'status':status})
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AddRating(CreateAPIView): # Post запрос на добавление рейтинга
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, users_id=pk)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(serializer.data)

class CommentModelViewSet(ModelViewSet): # CRUD на комменты
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        return serializer
    
class FavoriteModelViewSet(mixins.CreateModelMixin, #crud на избранные
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()

        # Comment.objects.filter(owner=self.request.user.id)

        queryset = queryset.filter(owner=self.request.user)
        return queryset