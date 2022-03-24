

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from board import views


router = DefaultRouter()
router.register('board', views.PostViewSet)
router.register('comment', views.CommentViewSet) # (댓글)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]