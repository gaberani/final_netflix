from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Comment
        fields = '__all__'