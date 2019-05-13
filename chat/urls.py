from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('messages/', views.messages, name='messages'),
    path('upload/', views.upload, name='views.upload'),
]

