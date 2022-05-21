from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.db import models
import os

User = get_user_model()


def mp3_upload_path(instance, filename):
    return os.path.join('MP3s/books', str(instance.code), filename)


class Book(models.Model):
    code = models.CharField(verbose_name='Book Code', max_length=20, unique=True)
    title = models.CharField(verbose_name='Book Title', max_length=255)
    mp3_file = models.FileField(verbose_name='Book MP3', upload_to=mp3_upload_path,
                                validators=[FileExtensionValidator(allowed_extensions=['mp3', ])])
    app_url = models.URLField(verbose_name='Book APP', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.code


class MyBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='user_book')
    review_url = models.CharField(verbose_name='Review URL', max_length=100, null=True, blank=True, unique=True)
    review_date = models.DateField(verbose_name='Review Date', null=True, blank=True)
    review_check = models.BooleanField(verbose_name='Review Check', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s : %s" % (self.user, self.book)

    class Meta:
        verbose_name = 'My Book'
        verbose_name_plural = 'My Books'


class BookQuestion(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='question_book')
    question = models.CharField(verbose_name='Question ?', max_length=255)
    answer = models.CharField(verbose_name='Answer ?', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book Question'
        verbose_name_plural = 'Book Questions'
