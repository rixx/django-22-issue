from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(state='deleted')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author, related_name='books')
    state = models.CharField(choices=(('regular', 'regular'), ('deleted', 'deleted')), default='regular', max_length=100)

    objects = BookManager()
