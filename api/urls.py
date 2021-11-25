from django.contrib import admin
from django.urls import path , include
from .views import CommentListApiView , CommentDetailApiView
urlpatterns = [
    path('', CommentListApiView.as_view()),
    path('<int:pk>', CommentDetailApiView.as_view()),
]
