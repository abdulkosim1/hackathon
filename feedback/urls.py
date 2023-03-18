from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register('comment', CommentModelViewSet)

urlpatterns = [  # adding like, rating, favorite
    path('<int:pk>/like/', AddLike.as_view()),
    path('', include(router.urls)),

    # path('<int:pk>/rating/', AddRating.as_view()),
    # path('favorite/', SongAddAndRemoveFavorite.as_view()),
]