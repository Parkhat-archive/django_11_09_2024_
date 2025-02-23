# Generated by Django 5.1.1 on 2024-09-11 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_alter_author_website_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(error_messages={'blank': 'Поле не может быть пустым'}, max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
