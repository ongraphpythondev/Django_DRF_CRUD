from django.contrib import admin
from django.urls import path , include
from .views import CommentListApiView , CommentDetailApiView


urlpatterns = [
# List view of all data in Comment db
    path('', CommentListApiView.as_view()),
# Detail view of specific data in Comment db
    path('<int:pk>', CommentDetailApiView.as_view()),
]
