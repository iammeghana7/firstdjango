from django.db import models
import uuid
import random
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    id=models.UUIDField(primary_key=True ,default=uuid.uuid4,help_text="generated unique id for book")
    name=models.CharField(max_length=100,help_text='Book Name',null=True)
    purchase_date=models.DateField(null=True,blank=True)
    
    book_author=models.ForeignKey('Author',on_delete=models.SET_NULL,help_text='Book Author' ,null=True)
    genre=models.ManyToManyField('Genre',help_text='genre of book')
    timestamp=models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'my_books'

    def __str__(self): #default method in all classes`
        return self.name

class Author(models.Model):
    
    author_name = models.CharField(max_length=100, help_text='Author Name',null=True)
    lang=models.CharField(max_length=100,help_text='Language' ,null=True)
    numchoice=(('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five'))
    total_book_written=models.CharField(max_length=100,choices=numchoice,null=True)
    date_of_birth=models.DateField('Birth',null=True,blank=True)
    date_of_death=models.DateField('Death',null=True,blank=True)
    timestamp=models.DateTimeField(auto_now=True)


    def __str__(self): #default method in all classes`
        return self.author_name 

class Genre(models.Model):
    
    name=models.CharField(max_length=100, help_text="Gener" ,null=True)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self): #default method in all classes`
        return self.name
        
class Student(models.Model):
    name=models.CharField(max_length=100,help_text="Student name",null=True)
    book_taken=models.ForeignKey('Book',help_text='Book',on_delete=models.CASCADE)
    author=models.ForeignKey('Author',help_text='Author of book',on_delete=models.CASCADE)
    numchoice=(('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five'))
    no_of_book_taken=models.CharField(max_length=100,choices=numchoice,null=True)
    Borrowed_date=models.DateField(default=timezone.now())
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Login(models.Model):
    username=models.CharField(max_length=30,)
    email=models.CharField(max_length=50,)
    password=models.CharField(max_length=50,)

    def __str__(self):
        return self.username



        