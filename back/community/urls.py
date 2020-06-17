from django.urls import path 
from . import views
app_name="articles"

urlpatterns=[
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/<int:comment_pk>/',views.comment_detail,name="comment_detail"),
    path('<int:article_pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/user_confirm/', views.user_confirm, name="user_confirm"),
    path('<int:article_pk>/article_update_and_delete/',views.article_update_and_delete,name='article_update_and_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/update_and_delete/',views.comments_update_and_delete,name='comments_update_and_delete'),
]