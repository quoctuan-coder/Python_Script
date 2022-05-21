from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('list/',views.view_question,name='view_list'),
    path('detail/<int:question_id>',views.detailView, name = 'detail'),
]
