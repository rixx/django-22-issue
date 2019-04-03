This repo documents a potential issue in Django 2.2.

Setup
-----

These steps were executed:

```
pip install django pytest pytest-django  # Installing Django 2.2.0 and deps
django-admin startproject fktest
cd fktest
python manage.py startapp fk  # Add to INSTALLED_APPS
# Add fk/models.py
python manage.py makemigrations
python manage.py migrate
python manage.py shell

from fk.models import Author, Book
a = Author.objects.create(name='Bill')
b1 = Book.objects.create(title='Sonnets', state='deleted', author=a)

b2 = Book.objects.create(title='Hamlet', author=a)
a.books.count()
a.books.all().count()


DJANGO_SETTINGS_MODULE=fktest.settings pytest
```
