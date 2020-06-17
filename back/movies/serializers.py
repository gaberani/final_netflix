from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie,Comment, Genre

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(required=False)
    class Meta:
        model=Comment
        fields=['id','rating', 'content', 'movie_id','user']

class MovieSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    movie_comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Movie
        fields='__all__'
        extra_fields=['movie_comments']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields="__all__"