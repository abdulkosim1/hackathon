# from post.models import Post
# from rest_framework.viewsets import ModelViewSet
# from feedback.models import Comment, Like, Rating
# from feedback.serializers import CommentSerializer, RatingSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import ListAPIView, CreateAPIView
# from post.serializers import PostSerializer


# class AddLike(CreateAPIView): # Post запрос на доваление лайков
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated,]
    
#     def post(self, request, pk, *args, **kwargs):
#         user = request.user
#         like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
#         like_obj.is_like = not like_obj.is_like
#         like_obj.save()
#         status = 'liked'
#         if not like_obj.is_like:
#             status = 'unliked'
#         return Response({'status':status})
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# # class AddRating(CreateAPIView): # Post запрос на добавление рейтинга
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated, ]

#     def post(self, request, pk, *args, **kwargs):
#         serializer = RatingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
#         rating_obj.rating = request.data['rating']
#         rating_obj.save()
#         return Response(serializer.data)

# # class SongAddAndRemoveFavorite(APIView): # Post запрос на добавление и удаление песен в избранных
# #     permission_classes = [IsAuthenticated]
# #     def post(self, request):
# #         song_id = request.data.get('song_id')
# #         try:
# #             song_id_a = Song.objects.get(id=song_id)
# #         except Song.DoesNotExist:
# #             return Response('Такой песни не существует :(', status=status.HTTP_404_NOT_FOUND)
# #         request.user.favorite_musics.add(song_id_a)
# #         return Response('Добавлено в избранное :)', status=200)

# #     def delete(self, request):
# #         song_id = request.data.get('song_id')
# #         try:
# #             song_id_a = Song.objects.get(id=song_id)
# #         except Song.DoesNotExist:
# #             return Response('Такой песни не существует :(', status=status.HTTP_404_NOT_FOUND)
# #         request.user.favorite_musics.remove(song_id_a)
# #         return Response('Удалено из избранного :)', status=200)


# # class SongAddAndRemoveFavorite(APIView): # Post запрос на добавление и удаление песен в избранных
# #     permission_classes = [IsAuthenticated]

# #     def post(self, request):
# #         post_id = request.data.get('id')
# #         try:
# #             song_id_a = Post.objects.get(id=post_id)
# #         except Post.DoesNotExist:
# #             return Response('Такой песни не существует :(', status=status.HTTP_404_NOT_FOUND)
# #         request.user.favorite_musics.add(song_id_a)
# #         return Response('Добавлено в избранное :)', status=200)

# #     def delete(self, request):
# #         post_id = request.data.get('id')
# #         try:
# #             song_id_a = Post.objects.get(id=post_id)
# #         except Post.DoesNotExist:
# #             return Response('Такой песни не существует :(', status=status.HTTP_404_NOT_FOUND)
# #         request.user.favorite_musics.remove(song_id_a)
# #         return Response('Удалено из избранных :)', status=200)


# # class CommentModelViewSet(ModelViewSet): # CRUD на комменты
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated,]

#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)
#         return serializer