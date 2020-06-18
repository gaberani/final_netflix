from django.shortcuts import render,get_object_or_404,get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Comment, Genre
from django.db.models import Q,Avg,Sum
from .serializers import MovieSerializer, MovieListSerializer, CommentSerializer, GenreSerializer 

# Get All Movies
@api_view(['GET'])
def index(request):
    
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies)
    return Response(serializer.data)
    
# Get Detail Movie
@api_view(['GET'])
def detail(request, movie_pk):  
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)

# Register Comments
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request,movie_pk): 
    serializer = CommentSerializer(data=request.data)
    comments = Comment.objects.filter(movie_id=movie_pk)
    users = []
    for comment in comments:
        if comment.user not in users:
            users.append(comment.user)
    if request.user not in users:
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie_id=movie_pk)
            return Response(serializer.data)
    else:
        return Response({'Messages': '이미 평점을 작성한 영화입니다.'})
    


# Recommend Movies
@api_view(['GET'])
def recommendMovies(request):
    comments=Comment.objects.filter(user=request.user).order_by('-rating')

    new_genres = {}
    for comment in comments:
        movie = get_object_or_404(Movie,id=comment.movie_id)
        
        serializer=MovieSerializer(movie)
        for genre in serializer.data['genres']:
            if genre not in new_genres:
                if comment.rating:
                    new_genres[genre] =comment.rating
            else:
                if comment.rating:
                    new_genres[genre] += comment.rating
    
    new_genres=sorted(new_genres.items(), key=lambda x:x[1],reverse=True)
    
    recommend={}

    # Genres Ordered By User Ratings
    for k,v in new_genres:
        movies=Movie.objects.filter(genres=k)
        # Movies in Genres
        for i in movies:
            total=0
            # Summation of Comments Ratings
            ratings=Comment.objects.filter(movie_id=i.id)
            if ratings:
                for k in ratings:
                    total+=ratings[0].rating
            if total:
                recommend[i.id]=total
    recommend=sorted(recommend.items(),key=lambda x:x[1],reverse=True)

    if len(recommend)<5:
        movie=Movie.objects.order_by("?")[:5]
        serializer=MovieSerializer(movie,many=True)
        
    else:
        result=[]
        for i in recommend[:5]:
            result.append(i[0])
        movie=Movie.objects.filter(id__in=result)
        serializer=MovieSerializer(movie,many=True)
    return Response(serializer.data)

# Update and Delete Comments
@api_view(['PUT', 'DELETE'])
def comment_update_and_delete(request,movie_pk,comment_pk):
    comment=get_object_or_404(Comment,pk=comment_pk)
    if request.user == comment.user:
        print('User OK')
        if request.method=='PUT':
            serializer=CommentSerializer(data=request.data,instance=comment)
            print('Method PUT')
            if serializer.is_valid(raise_exception=True):
                print('is_valid OK')
                serializer.save()
                return Response(serializer.data)
        else:
            print('Method DELETE')
            comment.delete()
            return Response({'message':'삭제 완료!'})
    else:
        return Response({'message': '다른 사용자는 불가합니다'})

# Popular Top3
@api_view(['GET'])
def many3(request):
    many3 = Movie.objects.order_by('-popularity')[:3]
    serializer = MovieSerializer(many3, many=True)
    return Response(serializer.data)

# Top Rated Top3
@api_view(['GET'])
def top3(request):
    top3 = Movie.objects.order_by('-vote_average')[:3]
    serializer = MovieSerializer(top3, many=True)
    return Response(serializer.data)

# Movie Search
@api_view(['GET'])
def search(request,movie_title):
    movie=Movie.objects.filter(title__contains=movie_title)
    if movie.exists():
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data)
    else:
        return Response({'message':'No Result'})

    
@api_view(['POST'])
def wannawatch(request, movie_pk):
    movie = get_object_or_404(Movie,id=movie_pk)
    if movie.like_users.filter(pk=request.user.id).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
    # return Response({'message': '필요없음'})

@api_view(['GET'])
def confirmWatch(request,movie_pk):
    movie=get_object_or_404(Movie,id=movie_pk)
    if request.user in movie.like_users.all():
        return Response({'result':1})
    else:
        return Response({'result':0})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getwannawatch(request):
    user=request.user
    movies=user.like_movies.all()
    serializer=MovieListSerializer(movies,many=True)
    return Response(serializer.data)

# Find All Genres
@api_view(['GET'])
def findgenre(request):
    genre=Genre.objects.all()
    serializer=GenreSerializer(genre,many=True)
    return Response(serializer.data)

# Find Specific Genres
@api_view(['GET'])
def getGenre(request,genre_id):
    movies=Movie.objects.filter(genres=genre_id)
    print(len(movies))
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)