import imp
from django.shortcuts import render

from rest_framework import generics
from .serializer import TodolistSerializer
from .models import TodoListApi


class TodoListCreateApiview(generics.ListCreateAPIView):
    queryset = TodoListApi.objects.all()
    serializer_class = TodolistSerializer

listcreateview = TodoListCreateApiview.as_view()

class TodoDetailApiview(generics.RetrieveAPIView):
    queryset = TodoListApi.objects.all()
    serializer_class = TodolistSerializer

detailview = TodoDetailApiview.as_view()


class TodoUpdateApiview(generics.UpdateAPIView):
    queryset = TodoListApi.objects.all()
    serializer_class = TodolistSerializer

updateview = TodoUpdateApiview.as_view()


class TodoDestroyApiview(generics.DestroyAPIView):
    queryset = TodoListApi.objects.all()
    serializer_class = TodolistSerializer

deleteview = TodoDestroyApiview.as_view()

