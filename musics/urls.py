from django.urls import path
from . import views

app_name = 'musics'
urlpatterns = [
    path('', views.list, name = 'list'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('detail/<int:id>/save_comment/', views.save_comment, name = 'save_comment'),
]