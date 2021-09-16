from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import Http404
from .models import Question, QuestionManager
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def home(request):
    pass


def popular(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.all(), limit)
    articles = paginator.page(page)
    return render(request, 'qa/popular.html', {'articles': articles})



def question(request, id):
    try:
        question = Question.objects.get(pk = id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'qa/question.html', {'question': question})
    # question = Question.objects.all()
    # return HttpResponse(question)