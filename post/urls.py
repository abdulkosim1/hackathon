from django.urls import path
from post.views import *

urlpatterns = [
    path('get_post/', PostListAPIView.as_view()),
    path('create_post/', PostCreateAPIView.as_view()),
    path('change/<int:id>/', PostRetriveUpdateDestroyAPIView.as_view()),


    # path('recom/', SystemOfRecomendation.as_view()),

]