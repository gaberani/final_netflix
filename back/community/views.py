from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer

# Get All Articles
@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# Create Article
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

# Get Detail Article
@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# Create Comment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comments_create(request,article_pk):    
    article=get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data)

# Get Detail Comment
@api_view(['GET'])
def comment_detail(request, article_pk,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

# Article Modify
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_update_and_delete(request,article_pk):
    article=get_object_or_404(Article,pk=article_pk)
    if request.user == article.user:
        if request.method=='PUT':
            serializer=ArticleSerializer(data=request.data, instance=article)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
        else:
            print('난 delete')
            article.delete()
            return Response({'message':'삭제 완료!'})
    else:
        return Response({'message': '다른 사용자는 불가합니다'})

# Comment Modify
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comments_update_and_delete(request, article_pk, comment_pk):
    article=get_object_or_404(Article,pk=article_pk)
    comment=get_object_or_404(Comment,pk=comment_pk)
    if comment.user == request.user:
        if request.method=='PUT':
            serializer=CommentSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, article=article)
                return Response(serializer.data)
            else:
                print(serializer.errors)
        else:
            comment.delete()
            return Response({'message':'삭제 완료!'})
    else:
        return Response({'message': '다른 사용자는 불가합니다'})

# Confirm User
@api_view(['GET'])
def user_confirm(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user == request.user:
        return Response({'isUser':True})
    else:
        return Response({'isUser':False})