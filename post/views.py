from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsExecutant
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from django.db.models import Avg
import logging

logger = logging.getLogger('main')

User = get_user_model()

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

    logger.info('get all posts')

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

# class SystemOfRecomendation(ListAPIView): # Get запрос на систему рекомендаций  
#     serializer_class = PostSerializer
#     permission_classes = []
#     pagination_class = CustomPagination
#     queryset = Post.objects.all()
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if Post.objects.filter(id=self.request.user.id):
#             return queryset