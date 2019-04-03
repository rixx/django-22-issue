import pytest

from fk.models import Author, Book


@pytest.fixture
def author():
    return Author.objects.create(name='Bill')


@pytest.fixture
def book(author):
    b = Book.objects.create(title='Hamlet')
    b.authors.add(author)
    return b


@pytest.fixture
def deleted_book(author):
    b = Book.objects.create(state='deleted', title='Sonnets')
    b.authors.add(author)
    return b


@pytest.mark.django_db
def test_reverse_lookups(author, book, deleted_book):
    assert author.books.all().count() == 1
    assert author.books.count() == 1
