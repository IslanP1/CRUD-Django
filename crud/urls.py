from django.urls import path
from crud import views

app_name = 'crud'

urlpatterns = [
    path('', views.ClienteLists.as_view(), name='list'),
    path('create/', views.ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete'),
  
]
