# Generated by Django 3.1.4 on 2021-03-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210302_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='writer',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(null=True, related_name='_author_book_+', to='api.Book', verbose_name='كتاب\u200cها'),
        ),
    ]
