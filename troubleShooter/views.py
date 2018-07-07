from django.shortcuts import render
from troubleShooter.models import Choice, Question
# Create your views here.
from django.http import HttpResponse


def index(request):
    count=Question.objects.all()
    return HttpResponse(count[0].question_text)