from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article,Comment

class ArticleListSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Article
        fields = ['id','content','title','user']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Comment
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'article')

class ArticleSerializer(serializers.ModelSerializer):
    article_comments=CommentSerializer(many=True,read_only=True)
    user = UserSerializer(required=False)
    class Meta:
        model=Article
        fields='__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
        extra_fields=['article_comments']
