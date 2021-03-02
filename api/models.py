import string
from django.contrib.auth.models import User
from django.db import models
import secrets


# This function will create a unique code for each book automatically.
def random_book_code():
    code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(12))
    if Book.objects.all().count() >= 1:
        code += str(Book.objects.all().count())
        return code
    else:
        return code + '00'


# Author Model
class Author(models.Model):
    class Meta:
        verbose_name = 'نويسنده'
        verbose_name_plural = 'نويسندگان'

    # Provide a user account for our author instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, verbose_name='كاربر')

    def __str__(self):
        return self.user.get_full_name() if self.user.first_name and self.user.last_name else self.user.username

    # Counting the number of each Author's books.
    def count_books(self):
        res = Book.objects.filter(author=self).count()
        return res

    count_books.short_description = 'تعداد كتاب‌هاي منتشر شده'


# Book Model
class Book(models.Model):
    class Meta:
        verbose_name = 'كتاب'
        verbose_name_plural = 'كتاب‌ها'

    title = models.CharField('عنوان', max_length=100, unique=True)
    code = models.CharField('كد شابك', max_length=25, default=random_book_code, blank=True)
    content = models.TextField('متن')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نويسنده')
    category = models.CharField('دسته‌بندي', max_length=40)

    def __str__(self):
        return self.title
