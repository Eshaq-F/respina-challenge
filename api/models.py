import string
from random import random

from django.contrib.auth.models import User
from django.db import models
import secrets


def random_book_code():
    code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(12))
    if Book.objects.all().count() >= 1:
        code += str(Book.objects.all().count())
        return code
    else:
        return code + '00'


class Author(models.Model):
    class Meta:
        verbose_name = 'نويسنده'
        verbose_name_plural = 'نويسندگان'

    books = models.ManyToManyField('Book', verbose_name='كتاب‌ها', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, verbose_name='كاربر')

    def __str__(self):
        return self.user.get_full_name() if self.user.first_name and self.user.last_name else self.user.username


class Book(models.Model):
    class Meta:
        verbose_name = 'كتاب'
        verbose_name_plural = 'كتاب‌ها'

    title = models.CharField('عنوان', max_length=100, unique=True)
    code = models.CharField('كد شابك', max_length=25, default=random_book_code, blank=True)
    content = models.TextField('متن')
    writer = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نويسنده')
    category = models.CharField('دسته‌بندي', max_length=40)

    def __str__(self):
        return self.title
