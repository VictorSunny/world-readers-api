from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()
class Category(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=255, unique= True)

    class Meta:
        ordering = ['title',]

    def __str__(self):
        return self.title


class BookDB(models.Model):

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.ForeignKey(Category, default= 1, on_delete=models.CASCADE, related_name= 'books')
    created_on = models.DateTimeField(auto_now_add= True, null= True)
    modified_on = models.DateTimeField(auto_now= True, null= True)
    created_by = models.ForeignKey(User, null= True, on_delete= models.DO_NOTHING, related_name= 'books')

    class Meta:
        ordering = ['-created_on',]

    def __str__(self):
        return self.name