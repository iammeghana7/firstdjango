from django.contrib import admin
from home.models import Book
from home.models import Author
from home.models import Genre,Student,Login
# Register your models here.



# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 #   search_fields=('id','name')
    
    list_filter=('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))
    #list_filter=('name','purchase_date','book_author')
    


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass