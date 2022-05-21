import json

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.models import Book, MyBook, BookQuestion
from dashboard.forms import CreateBookForm, UpdateBookForm
from dashboard.mixins import SuperUserRequiredMixin

import datetime

REVIEW_URLS = [
    'amazon.com',
    'amazon.in',
    'amazon.co.uk',
    'amazon.de',
    'amazon.fr',
    'amazon.es',
    'amazon.it',
    'amazon.nl',
    'amazon.co.jp',
    'amazon.com.br',
    'amazon.ca',
    'amazon.com.mx',
    'amazon.com.au',
]


def get_rotate_questions(book_questions):
    day_today = datetime.datetime.today().day
    days_question1 = [1, 11, 21, 31]
    days_question2 = [2, 12, 22]
    days_question3 = [3, 13, 23]
    days_question4 = [4, 14, 24]
    days_question5 = [5, 15, 25]
    days_question6 = [6, 16, 26]
    days_question7 = [7, 17, 27]
    days_question8 = [8, 18, 28]
    days_question9 = [9, 19, 29]
    days_question10 = [10, 20, 30]

    if day_today in days_question1:
        return book_questions[0]
    elif day_today in days_question2:
        return book_questions[1]
    elif day_today in days_question3:
        return book_questions[2]
    elif day_today in days_question4:
        return book_questions[3]
    elif day_today in days_question5:
        return book_questions[4]
    elif day_today in days_question6:
        return book_questions[5]
    elif day_today in days_question7:
        return book_questions[6]
    elif day_today in days_question8:
        return book_questions[7]
    elif day_today in days_question9:
        return book_questions[8]
    elif day_today in days_question10:
        return book_questions[9]
    else:
        return None


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            queryset = MyBook.objects.all().order_by('-created_at')
        else:
            queryset = MyBook.objects.filter(user=self.request.user).order_by('-created_at')
        context['queryset'] = queryset
        context['books'] = Book.objects.all().order_by('-created_at')
        return context


class BooksView(SuperUserRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/books.html'

    def get_queryset(self):
        return Book.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        context['form_create'] = CreateBookForm()
        context['form_update'] = UpdateBookForm()
        return context


class CreateBookView(SuperUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'dashboard/books.html'
    success_url = reverse_lazy('dashboard:books')
    success_message = 'Your Book has been added successfully'

    def form_invalid(self, form):
        json_errors = form.errors.as_json()
        json_errors = json.loads(json_errors)
        for key in json_errors:
            msg_error = json_errors[key][0]['message']
            messages.error(self.request, msg_error)

        return redirect('dashboard:books')


class UpdateBookView(SuperUserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    form_class = UpdateBookForm
    template_name = 'dashboard/books.html'
    success_url = reverse_lazy('dashboard:books')
    success_message = 'Your Book has been updated successfully'

    def form_invalid(self, form):
        json_errors = form.errors.as_json()
        json_errors = json.loads(json_errors)
        for key in json_errors:
            msg_error = json_errors[key][0]['message']
            messages.error(self.request, msg_error)

        return redirect('dashboard:books')


class DeleteBookView(SuperUserRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_id = kwargs.get('book_id')
            book = Book.objects.filter(id=book_id).first()
            if book:
                book.delete()
                json_response['success'] = True
                json_response['message'] = 'Your Book has been deleted successfully'
            else:
                json_response['message'] = 'This book does not exist'

        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while removing the book, please try again'

        return JsonResponse(json_response)


class BookQuestionsView(SuperUserRequiredMixin, ListView):
    model = BookQuestion
    context_object_name = 'questions'
    template_name = 'dashboard/questions.html'

    def get_context_data(self, **kwargs):
        context = super(BookQuestionsView, self).get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        book = Book.objects.get(id=book_id)
        context['book_code'] = book.code
        return context

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return BookQuestion.objects.filter(book_id=book_id).order_by('-created_at')


class GetBookQuestionsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_id = kwargs.get('book_id')
            book_questions = BookQuestion.objects.filter(book_id=book_id).order_by('created_at')
            book_question = get_rotate_questions(book_questions)
            if book_question:
                json_response['data'] = {'question': book_question.question, 'id': book_question.id}
                json_response['success'] = True
            else:
                json_response['message'] = 'This Book has no questions yet'

        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while getting the questions of this book'

        return JsonResponse(json_response)


class ProofBookByAnswerQuestionView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_question_id = self.kwargs.get('book_question_id')
            answer = request.POST['answer']
            book_question = BookQuestion.objects.get(id=book_question_id)
            if book_question:
                if book_question.answer == answer:
                    MyBook.objects.create(user=request.user, book=book_question.book)
                    json_response['success'] = True
                    msg = "Your Book has been added successfully to your list 'My-Books'"
                    messages.success(request, msg)
                else:
                    json_response['message'] = 'Wrong answer - Please try again.'
            else:
                json_response['message'] = 'Error while getting the questions of this book.'

        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while adding the book to your list, please try again'

        return JsonResponse(json_response)


class CreateQuestionView(SuperUserRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_id = self.kwargs.get('book_id')
            question = request.POST['question']
            answer = request.POST['answer']
            count_books = BookQuestion.objects.filter(book_id=book_id).count()
            if count_books >= 10:
                json_response['message'] = 'You have saved more than 10 questions for this book ... ' \
                                           'please remove one question before you add a new one !'
            else:
                book_question = BookQuestion.objects.create(question=question, answer=answer, book_id=book_id)
                book_question_dict = model_to_dict(book_question)
                book_question_dict['book'] = book_question.book.code
                json_response['book_question'] = book_question_dict
                json_response['success'] = True
                json_response['message'] = 'Your Question has been added successfully'
        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while saving the question, please try again'

        return JsonResponse(json_response)


class UpdateQuestionView(SuperUserRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_question_id = kwargs.get('book_question_id')
            question = request.POST['question']
            answer = request.POST['answer']

            book_question = BookQuestion.objects.get(id=book_question_id)
            book_question.question = question
            book_question.answer = answer
            book_question.save()
            json_response['success'] = True
            json_response['message'] = 'Your Question has been updated successfully'
        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while updating the question, please try again'

        return JsonResponse(json_response)


class DeleteQuestionView(SuperUserRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_question_id = kwargs.get('book_question_id')
            book_question = BookQuestion.objects.filter(id=book_question_id).first()
            if book_question:
                book_question.delete()
                json_response['success'] = True
                json_response['message'] = 'Your Question has been deleted successfully'
            else:
                json_response['message'] = 'This Question does not exist'

        except Exception as e:
            json_response['error'] = str(e)
            json_response['message'] = 'Error while removing the question, please try again'

        return JsonResponse(json_response)


class BookReviewUrlsView(SuperUserRequiredMixin, ListView):
    model = MyBook
    context_object_name = 'queryset'
    template_name = 'dashboard/review_urls.html'

    def get_queryset(self):
        unvalidated = self.request.GET.get('unvalidated')
        if unvalidated:
            queryset = MyBook.objects.filter(review_check=False).order_by('-created_at')
        else:
            queryset = MyBook.objects.all().order_by('-created_at')
        return queryset


class CheckReviewBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False, "redirect_app": 0}
        try:
            book_id = self.kwargs.get('book_id')
            my_book = MyBook.objects.get(id=book_id)
            has_review_url = True if my_book.review_url else False
            if my_book.review_check:
                json_response['redirect_app'] = 1
                json_response['app_url'] = my_book.book.app_url
                messages.success(request, 'Your App will be downloaded in a moment ..')
            if not my_book.review_check and has_review_url:
                messages.info(request, 'Within 24 hours, we will activate your App download link .. Please wait.')
            if not my_book.review_check and not has_review_url:
                json_response['book_code'] = my_book.book.code
            json_response['success'] = True
        except Exception as e:
            print(e)
            json_response['error'] = str(e)

        return JsonResponse(json_response)


class SubmitReviewBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_id = self.kwargs.get('book_id')
            review_url = self.request.POST['review_url']
            my_book = MyBook.objects.get(id=book_id)
            is_valid_review_url = any(url in review_url for url in REVIEW_URLS)
            if is_valid_review_url:
                my_book.review_url = review_url
                my_book.save()
                msg = 'Thank you! Within 24 hours, we will activate your App download link.'
                messages.info(request, msg)
                json_response['success'] = True
            else:
                msg = 'Sorry, The review link submitted is not valid.'
                json_response['success'] = False
                json_response['error'] = msg
        except Exception as e:
            print(e)
            msg = 'Sorry, This review link has been previously submitted.'
            json_response['error'] = msg

        return JsonResponse(json_response)


class ValidateReviewBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        json_response = {"success": False}
        try:
            book_id = self.kwargs.get('book_id')
            my_book = MyBook.objects.get(id=book_id)
            if not my_book.review_url:
                msg = 'This book need a ReviewURL !'
                messages.warning(request, msg)
            else:
                my_book.review_check = True
                my_book.review_date = datetime.date.today()
                my_book.save()

                # send mail to user
                context_mail = {'app_url': my_book.book.app_url}
                subject = 'Korabko - Your App Book Url Is Ready'
                text_content = render_to_string('mails/validate_review_url.txt', context_mail)
                html_content = render_to_string('mails/validate_review_url.html', context_mail)
                msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[my_book.user.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                msg = 'The ReviewURL of book ' + my_book.book.code + ' has been validated successfully.'
                messages.success(request, msg)
            json_response['success'] = True
        except Exception as e:
            json_response['error'] = str(e)
            messages.error(request, str(e))

        return JsonResponse(json_response)


class ReportsView(SuperUserRequiredMixin, TemplateView):
    template_name = 'dashboard/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        model_name = self.kwargs.get('model_name')
        if model_name == 'book':
            context['books'] = Book.objects.all().order_by('-created_at')
        if model_name == 'review-url':
            unvalidated = self.request.GET.get('unvalidated')
            if unvalidated:
                context['review_urls'] = MyBook.objects.filter(review_check=False).order_by('-created_at')
            else:
                context['review_urls'] = MyBook.objects.all().order_by('-created_at')
        if model_name == 'question':
            context['questions'] = BookQuestion.objects.all().order_by('-created_at')

        return context