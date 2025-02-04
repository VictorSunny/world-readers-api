from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers, models
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class UserCreationView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer


    @swagger_auto_schema(
        operation_summary= 'creates a new user for authentication'
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data= data)

        if serializer.is_valid():
            serializer.save()

            return Response(data= serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)