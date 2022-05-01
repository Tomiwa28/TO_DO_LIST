from unicodedata import name
from django.urls import path
from .views import tasklist, taskdetail, taskcreate,taskupdate, taskdelete, MyLoginview, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path('accounts/login/',MyLoginview.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('Register/',RegisterPage.as_view(), name ='Register'),
    path('',tasklist.as_view(), name = 'tasks'),
    path('task/<int:pk>/',taskdetail.as_view(), name = 'tasks'),
    path('task_create/',taskcreate.as_view(), name = 'task_create'),
    path('task_update/<int:pk>/' , taskupdate.as_view(), name = 'task_update'),
    path('task_delete/<int:pk>/' , taskdelete.as_view(), name = 'task_delete'),


]