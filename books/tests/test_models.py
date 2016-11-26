from django.test import TestCase
from books.models import Book
from books.factories import AuthorFactory


# class DemoTest(TestCase):
#
#     def test_addition(self):
#         self.assertEqual(1 + 1, 4)

class BookTest(TestCase):

    def setUp(self):
        self.author_one = AuthorFactory(name="Author 1")
        self.author_two = AuthorFactory(name="Author 2")

        self.book = Book(title="My Book")
        self.book.save()
        self.book.authors.add(self.author_one.pk, self.author_two.pk)

    def tearDown(self):
        self.author_one.delete()
        self.author_two.delete()
        self.book.delete()

    def test_can_list_authors(self):
        self.assertEqual("Author 1, Author 2", self.book.list_authors())

    def test_string_method(self):
        self.assertEqual("My Book by Author 1, Author 2", self.book.__str__())

    def test_custom_save_method(self):
        self.assertIsNone(self.book.date_reviewed)
        self.book.review = "My not so lengthy review"
        self.book.save()
        self.assertIsNotNone(self.book.date_reviewed)