import pytest

from fk.models import Author, Book


@pytest.fixture
def author():
    return Author.objects.create(name='Bill')


@pytest.fixture
def book(author):
    return Book.objects.create(title='Hamlet', author=author)


@pytest.fixture
def deleted_book(author):
    return Book.objects.create(state='deleted', title='Sonnets', author=author)


@pytest.mark.django_db
def test_reverse_lookups(author, book, deleted_book):
    assert author.books.count() == 1
    assert author.books.all().count() == 1
