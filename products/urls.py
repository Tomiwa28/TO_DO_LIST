from django.urls import path

from . import views

urlpatterns = [
    path('', views.listcreateview),
    path('<int:pk>/', views.detailview),
    path('update/', views.updateview),
    path('delete/<int:pk>/', views.deleteview),
]