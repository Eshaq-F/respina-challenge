# Generated by Django 3.1.4 on 2021-03-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210228_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, to='api.Book', verbose_name='كتاب\u200cها'),
        ),
    ]