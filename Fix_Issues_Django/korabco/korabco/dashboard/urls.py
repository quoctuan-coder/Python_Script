from django.urls import path

from dashboard.views import (
    DashboardView,
    BooksView,
    CreateBookView,
    UpdateBookView,
    DeleteBookView,
    BookReviewUrlsView,
    CheckReviewBookView,
    SubmitReviewBookView,
    ValidateReviewBookView,
    GetBookQuestionsView,
    ProofBookByAnswerQuestionView,
    BookQuestionsView,
    CreateQuestionView,
    UpdateQuestionView,
    DeleteQuestionView,
    ReportsView,
)

app_name = "dashboard"


urlpatterns = [
    path(route='', view=DashboardView.as_view(), name='home'),

    path(route='books/', view=BooksView.as_view(), name='books'),
    path(route='book/create/', view=CreateBookView.as_view(), name='create_book'),
    path(route='book/<pk>/update/', view=UpdateBookView.as_view(), name='update_book'),
    path(route='book/<book_id>/delete/', view=DeleteBookView.as_view(), name='delete_book'),

    path(route='book/<book_id>/questions/', view=BookQuestionsView.as_view(), name="book_questions"),
    path(route='book/<book_id>/get/questions/', view=GetBookQuestionsView.as_view(), name="book_get_questions"),
    path(route='book/<book_id>/question/create/', view=CreateQuestionView.as_view(), name='create_question'),
    path(route='book/question/<book_question_id>/update/', view=UpdateQuestionView.as_view(), name='update_question'),
    path(route='book/question/<book_question_id>/delete/', view=DeleteQuestionView.as_view(), name='delete_question'),
    path(route='book/question/<book_question_id>/proof/', view=ProofBookByAnswerQuestionView.as_view(), name="proof_book"),

    path(route='book/review-urls/', view=BookReviewUrlsView.as_view(), name="book_review_urls"),
    path(route='book/<book_id>/check/review-url/', view=CheckReviewBookView.as_view(), name='check_review_book'),
    path(route='book/<book_id>/submit/review-url/', view=SubmitReviewBookView.as_view(), name='submit_review_book'),
    path(route='book/<book_id>/validate/review-url/', view=ValidateReviewBookView.as_view(), name='validate_review_book'),

    path(route='<model_name>/reports/', view=ReportsView.as_view(), name='reports'),

]
