from rest_framework import serializers
from api.models import Comment

# serializing Comment db's data
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','msg' , 'user' , 'created_on']