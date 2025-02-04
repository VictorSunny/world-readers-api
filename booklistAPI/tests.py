from django.test import TestCase
import requests

# Create your tests here.

#signup config
# url = 'http://localhost:8000/auth/jwt/create/'
# json = {"email": "admin@dj.com", "password": "admin"}
# url = 'http://localhost:8000/api/books/2'

#authorization config
header = {
    "Content-type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5MTE1ODgwLCJpYXQiOjE3Mzg1MTEwODAsImp0aSI6IjgzMTgzNWIzZDcxMTRiMjE5ODE2YzA5NzY3MzgxMzIyIiwidXNlcl9pZCI6MX0.vGtgPg3QXzi6uJu62qPdFuK3LIU_S3XaV6GsN3NhVsw"
    }

#post test

json = {
    'name': 'Purple hibiscus',
    'author': 'Chimamanda Adichie',
    'year': 2003,
    'category_id': 'Play'
}

# edit
# json = {
#     'name': 'TERMINATOR',
#     'author': 'tech people',
#     'year': 1992,
# }

# url = 'http://localhost:8000/api/books/3/'
# output = requests.delete(url= url, headers= header).text
# print(output)

url = 'http://localhost:8000/world-readers/v1/books/categories/comic/'
# json = {
#     'email': 'pytester1@gmail.com',
#     'username': 'pytester1',
#     'first_name': 'john', 
#     'last_name': 'doe',
#     'password': '@Bcd1234'
# }
output = requests.get(url= url, headers= header)
print(output.text)