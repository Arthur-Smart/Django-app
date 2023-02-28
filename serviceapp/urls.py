from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    # path('search', views.search, name='search'),
    path('upload', views.upload, name="upload" ),
    path('register', views.register, name="register" ),
    path('login', views.login, name="login" ),
    path('like', views.like, name="like"),
    path('follow', views.follow, name="follow"),
    path('profile/<str:pk>', views.profile, name="profile" ),
    path('service', views.service, name="service" ),
    path('account/<str:pk>', views.account, name="account" ),
    path('update', views.update, name="update" ),
    path('logout', views.logout, name="logout"),
    path('comment', views.comment, name='comment'),
    path('delete', views.delete_post, name='delete'),
    path('delete-comment', views.delete_comment, name='delete-comment'),
    path('post/<str:pk>', views.single_post, name='post'),
    path('search', views.search, name="search")
]