from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsExecutant

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsExecutant,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsExecutant,]
    lookup_field='id'
