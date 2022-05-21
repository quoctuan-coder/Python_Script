from .models import Question
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    myname = 'Tuan'
    taisan = ['DienThoai','MayTinh','Tien']

    context = {'name': myname, 'taisan':taisan}

    return render(request,'polls/index.html',context)

def view_question(request):
    list_question = Question.objects.all()

    context = {"dsquest" : list_question }

    return render(request,'polls/question_list.html',context)

def detailView(request,question_id):
    q = Question.objects.get(pk = question_id)
    return render(request,"polls/detail_question.html",{'qs':q})

def vote(request,question_id):
    q = Question.objects.get(pk = question_id)
    dulieu = request.POST["choice"]
    return HttpResponse(dulieu)