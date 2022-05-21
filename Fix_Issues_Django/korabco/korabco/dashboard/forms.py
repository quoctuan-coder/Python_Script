from django.forms import ModelForm
from dashboard.models import Book


class CreateBookForm(ModelForm):
    prefix = 'create'

    class Meta:
        model = Book
        fields = ('code', 'title', 'app_url', 'mp3_file')


class UpdateBookForm(ModelForm):
    prefix = 'update'

    class Meta:
        model = Book
        fields = ('code', 'title', 'app_url', 'mp3_file')