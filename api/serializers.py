from rest_framework import serializers
from api.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['msg' , 'user' , 'created_on']