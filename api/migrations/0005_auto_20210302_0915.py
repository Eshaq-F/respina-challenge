# Generated by Django 3.1.4 on 2021-03-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210302_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='writer',
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, to='api.Book', verbose_name='كتاب\u200cها'),
        ),
    ]
