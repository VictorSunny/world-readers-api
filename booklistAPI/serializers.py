from rest_framework import serializers
from . models import BookDB, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class BookDBSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=150)
    year = serializers.IntegerField()

    category = CategorySerializer(read_only= True)
    category_id = serializers.IntegerField(write_only= True)

    class Meta:
        model = BookDB
        fields = ['name', 'author', 'year', 'category', 'category_id']

class SingleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDB
        fields = ['name', 'author', 'year', 'category', 'created_on', 'modified_on']

