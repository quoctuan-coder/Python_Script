from django.contrib import admin
from dashboard.models import Book, MyBook, BookQuestion


class BookAdmin(admin.ModelAdmin):

    list_display = ('code', 'title', 'app_url', 'created_at', 'updated_at')
    search_fields = ('code', 'title')


admin.site.register(Book, BookAdmin)


class MyBookAdmin(admin.ModelAdmin):

    list_display = ('user', 'book', 'review_url', 'review_date', 'review_check')
    search_fields = ('review_url', 'title')


admin.site.register(MyBook, MyBookAdmin)


class BookQuestionAdmin(admin.ModelAdmin):

    list_display = ('book', 'question', 'answer')
    search_fields = ('book__code', )


admin.site.register(BookQuestion, BookQuestionAdmin)
