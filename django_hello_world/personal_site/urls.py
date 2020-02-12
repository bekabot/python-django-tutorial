from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_title>/detail/', views.detail, name='detail'),
    path('<int:post_title>/like/', views.like, name='like'),
]
