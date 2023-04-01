from django.urls import reverse
from django.test import TestCase

class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response , 'No books found.')
