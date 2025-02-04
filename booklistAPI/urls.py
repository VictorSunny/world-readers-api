from django.urls import path
from . import views

app_name = 'booklistAPI'

urlpatterns = [
    path('books/', views.BooksView.as_view(), name= 'api-home'),
    path('books/<int:book_id>/', views.BookUpdateView.as_view(), name= 'book-update'),
    path('books/categories/', views.CategoryView.as_view(), name= 'categories'),
    path('books/categories/<str:name>/', views.CategoryBooksView.as_view(), name= 'category-books'),
]