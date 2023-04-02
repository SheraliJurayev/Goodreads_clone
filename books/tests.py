from django.urls import reverse
from django.test import TestCase

from books.models import Book

class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response , 'No books found.')

    def test_books_list(self):
        Book.objects.create(title='test title1', description = 'test description1' , isbn = '111111111111')
        Book.objects.create(title='test title2', description = 'test description2' , isbn = '222222222222')
        Book.objects.create(title='test title3', description = 'test description3' , isbn = '333333333333')

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()

        for book in books:
            self.assrertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title='test title1', description = 'test description1' , isbn = '111111111111')

        response = self.client.get(reverse('books:detail' , kwargs={'id':book.id}))        

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
        self.assertContains(response, book.isbn)


