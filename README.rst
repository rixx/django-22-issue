This repo documents a potential issue in Django 2.2.

Reproduce the issue
-------------------

Either via tests::

  pip install django pytest pytest-django
  cd fktest
  DJANGO_SETTINGS_MODULE=fktest.settings pytest


Or via the Python REPL::

  python manage.py makemigrations
  python manage.py migrate
  python manage.py shell

  from fk.models import Author, Book
  a = Author.objects.create(name='Bill')
  b1 = Book.objects.create(title='Sonnets', state='deleted')
  b2 = Book.objects.create(title='Hamlet')
  b1.authors.add(a)
  b2.authors.add(a)
  a.books.count()  # 2
  a.books.all().count()  # 1
