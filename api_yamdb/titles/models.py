from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=256, requires=True)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256, requires=True)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название', max_length=256, requires=True)
    slug = models.SlugField(unique=True, db_index=True)
    description =
    category = 
    genre = 
    date = 

    class Meta:
        ordering = ['name']
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return self.name
