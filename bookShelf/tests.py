from django.test import TestCase

from bookShelf.models import Author


def test1():
    author = Author
    author.name = "Igor"

