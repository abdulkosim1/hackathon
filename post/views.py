from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsExecutant
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomPagination(PageNumberPagination): # Кастомная пагинация
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 20

class PostListAPIView(generics.ListAPIView): # Просмотр постов 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title']
    search_fields = ['title', ]
    ordering_fileds = ['id','owner']

class PostCreateAPIView(generics.CreateAPIView): # Добавление постов
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsExecutant,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # Удаление, изменение постов
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsExecutant,]
    lookup_field='id'
