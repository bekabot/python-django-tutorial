from django.urls import path

from . import views

app_name = 'personal_site'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:post_title>/detail/', views.detail, name='detail'),
    path('<int:post_title>/like/', views.like, name='like'),
    path('add/', views.add, name='add'),
]
