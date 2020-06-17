from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
  path('', views.index,name='index'),
  path('comments/',views.comments, name="comments"),
  path('getGenre/<int:movie_id>/',views.getGenre,name="getGenre"),
  path('<int:movie_pk>/create/',views.create,name='create'), # 댓글
  path('<int:movie_pk>/',views.detail,name='detail'),
  path('many3/', views.many3,name='many3'),
  path('top3/', views.top3, name='top3'),
  path('<int:movie_pk>/comments/<int:comment_pk>/update_and_delete/',views.comment_update_and_delete,name="comment_update_and_delete"),
  path('search/<str:movie_title>/',views.search,name='search'),
  path('genre/',views.findgenre,name="findgenre"),
  path('genre/<int:genre_id>',views.prefergenre,name="prefergenre"),
  path('getwannawatch/',views.getwannawatch,name="getwannawatch"),
]