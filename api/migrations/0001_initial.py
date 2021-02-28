# Generated by Django 3.1.4 on 2021-02-28 11:31

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('code', models.CharField(blank=True, default=api.models.random_book_code, max_length=25, verbose_name='كد شابك')),
                ('content', models.TextField(verbose_name='متن')),
                ('category', models.CharField(max_length=40, verbose_name='دسته\u200cبندي')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author', verbose_name='نويسنده')),
            ],
            options={
                'verbose_name': 'كتاب',
                'verbose_name_plural': 'كتاب\u200cها',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='api.Book', verbose_name='كتاب\u200cها'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='كاربر'),
        ),
    ]
