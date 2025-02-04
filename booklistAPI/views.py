from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import serializers
from . models import BookDB, Category
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from drf_yasg.utils import swagger_auto_schema

class BooksView(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = serializers.BookDBSerializer
    queryset = BookDB.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(
            operation_summary= 'Retrieves all books from database for display',
                 operation_description= 'URL supports further filtering with params; "year" and "category", as well as "search" which checks for matching strings in book title'
    )
    def get(self, request):

        books = BookDB.objects.all()

        category_name = request.query_params.get('category')
        year_published = request.query_params.get('year')
        search = request.query_params.get('search')

        if category_name:
            books = BookDB.objects.filter(category= get_object_or_404(Category, title= category_name))
        if year_published:
            books = BookDB.objects.filter(year= year_published)
        if search:
            books = BookDB.objects.filter(name__icontains= search)

        serializer = self.serializer_class(instance= books, many= True)
        return Response(data= serializer.data, status= status.HTTP_200_OK)
    

    @swagger_auto_schema(
        operation_summary= 'Creates a new book model entry inside database'
    )
    def post(self, request):
        data = request.data
        try:
            data['category_id'] = get_object_or_404(Category, title= data['category_id']).id
        except:
            new_category = Category.objects.create(title= data['category_id'], slug= data['category_id'])
            new_category.save()
            data['category_id'] = get_object_or_404(Category, title= data['category_id']).id
        
        serializer = self.serializer_class(data= data)

        if serializer.is_valid():
            serializer.save(created_by= request.user)

            return Response(data= serializer.data, status= status.HTTP_201_CREATED)
        

class BookUpdateView(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = serializers.SingleBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(
        operation_summary= 'Retrieves extensive information on a single book model instance',
    )
    def get(self, request, book_id):
        book = get_object_or_404(BookDB, id = book_id)

        serializer = self.serializer_class(instance= book)

        return Response(data= serializer.data, status= status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_summary= 'Updates an exisiting book instance with user input'
    )
    def put(self, request, book_id):
        book = get_object_or_404(BookDB, id = book_id)
        data = request.data
        serializer = self.serializer_class(instance= book, data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status= status.HTTP_205_RESET_CONTENT)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_summary= 'Deletes an exisiting book model instance from database'
    )
    def delete(self, request, book_id):
        book = get_object_or_404(BookDB, id = book_id)

        book.delete()

        return Response(data= status.HTTP_200_OK)
    

class CategoryView(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(
        operation_summary= 'Retrieves all available genres(categories) of books available'
    )
    def get(self, request):

        all_categories = Category.objects.all()
        serializer = self.serializer_class(instance= all_categories, many= True)

        return Response(data= serializer.data, status= status.HTTP_200_OK)
    
class CategoryBooksView(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = serializers.BookDBSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(
        operation_summary= 'Retrieves all books related to the specified category in url'
    )
    def get(self, request, name):

        category_id = get_object_or_404(Category, title= name)
        data = BookDB.objects.filter(category= category_id)
        serializer = self.serializer_class(instance= data, many= True)

        return Response(data= serializer.data, status= status.HTTP_200_OK)