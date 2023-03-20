from django.test import TestCase
from .models import Book


class TestAPI(TestCase):
    def setUp(self):
        self.book0 = Book.objects.create(title='a', genre='science')
        self.book1 = Book.objects.create(title='b', genre='science')
        self.book2 = Book.objects.create(title='c', genre='science')
        self.book3 = Book.objects.create(title='d', genre='drama')
        self.book4 = Book.objects.create(title='e', genre='drama')
        self.book5 = Book.objects.create(title='f', genre='science')
        self.book6 = Book.objects.create(title='g', genre='fiction')
        self.book7 = Book.objects.create(title='h', genre='fiction')

    def test_title(self):
        response = self.client.get('/books/science/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result.get('title'), 'List of Books')

    def test_genre(self):
        response = self.client.get('/books/drama/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result.get('genre'), 'drama')

    def test_list_of_books(self):
        response = self.client.get('/books/fiction/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(result.get('books'), [self.book6.id, self.book7.id])

    def test_wrong_genre(self):
        response = self.client.get('/books/quera/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(result.get('books'), [])