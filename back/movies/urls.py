from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
  path('', views.index,name='index'),# Get All Movies
  path('<int:movie_pk>/',views.detail,name='detail'),# Get Detail Movie

  path('<int:movie_pk>/create/',views.create,name='create'), # Register Comments
  path('<int:movie_pk>/comments/<int:comment_pk>/update_and_delete/',views.comment_update_and_delete,name="comment_update_and_delete"),# Update and Delete Comments,

  path('recommendMovies/',views.recommendMovies, name="recommendMovies"),# Recommend Movies
 
  path('many3/', views.many3,name='many3'), #PopularTop3
  path('top3/', views.top3, name='top3'), #TopRate Top3
  
  path('search/<str:movie_title>/',views.search,name='search'), #Search Movies

  path('genre/',views.findgenre,name="findgenre"),# Find All Genres
  path('getGenre/<int:genre_id>/',views.getGenre,name="getGenre"),# Find Specific Genres

  path('wannawatch/<int:movie_pk>/',views.wannawatch,name="wannawatch"),
  path('getwannawatch/',views.getwannawatch,name="getwannawatch"),
  path('confirmWatch/<int:movie_pk>/',views.confirmWatch,name='confirmWatch')
]