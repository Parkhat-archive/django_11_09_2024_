# Generated by Django 5.1.1 on 2024-09-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_alter_author_email_alter_author_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(error_messages={'blank': 'Поле не может быть пустым'}, max_length=10),
        ),
    ]
