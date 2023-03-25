from django.contrib import admin
from .models import Book ,Author, BookAuthor , BookReview 
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields =('title'  , 'isbn')
    list_display = ('title' , 'discription' ,'isbn' )

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class BookReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book , BookAdmin)
admin.site.register(Author , AuthorAdmin)
admin.site.register(BookAuthor , BookAuthorAdmin)
admin.site.register(BookReview , BookReviewAdmin)