from django.contrib import admin
from django.urls import path , include
from .views import CommentListApiView
urlpatterns = [
    path('', CommentListApiView.as_view()),
]
