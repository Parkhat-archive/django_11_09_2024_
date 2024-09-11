from django.contrib.auth.password_validation import MinimumLengthValidator
from django.db import models
from django.core.validators import MinLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=200)   # столбец title с типом данных VARCHAR(200)
    author = models.CharField(max_length=200,
                              null = True, blank = False,
                              error_messages={'blank':'Поле не может быть пустым'},
                              validators = [MinLengthValidator(5)])



    published_date = models.DateField()        # столбец published_date с типом данных DATE
    website = models.URLField(null = True, blank = True)
    GENGE_CHOICE = [
        ('fantasy', 'Fantasy'),
        ('love', 'Love'),
        ('science', 'Science'),
    ]
    genre = models.CharField(max_length = 10, null = True, choices = GENGE_CHOICE, default="No genre")
    book_presentation = models.CharField(unique_for_date='published_date', max_length = 100, default='None')



class Author(models.Model):
    name = models.CharField(primary_key=True, max_length = 100, verbose_name= "Имя")
    email = models.EmailField(max_length = 100, unique=True, help_text = "введите мэйл", db_index=True)
    website = models.URLField(max_length = 100)






