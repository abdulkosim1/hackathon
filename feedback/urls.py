from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register('comment', CommentModelViewSet)
router.register('favorite', FavoriteModelViewSet)


urlpatterns = [  # adding like, rating, favorite
    path('<int:pk>/like/', AddLike.as_view()),
    path('<int:pk>/rating/', AddRating.as_view()),
    # path('favorite/', FavoriteModelViewSet.as_view({'post':'create'})),

    path('', include(router.urls)),
]