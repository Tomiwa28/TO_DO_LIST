from rest_framework import serializers

from .models import TodoListApi

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListApi
        fields = [
            'id',
            'title',
            'Description',
            'complete',
            'create',
        ]