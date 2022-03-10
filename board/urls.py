from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [

  
  # community
  path('', views.community, name='community'),
  path('<int:pk>/', views.detail, name='detail'),
  path('write/', views.write, name='write'),
  path('create/', views.create, name='create'),
  path('<int:pk>/edit/', views.edit, name='edit'),
  path('<int:pk>/update', views.update, name='update'),
  path('<int:pk>/delete', views.delete, name='delete'),
]
