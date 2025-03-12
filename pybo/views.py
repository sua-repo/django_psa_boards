from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse(r"<h1>안녕하세요.</h1> <br> 게시판을 만들겠습니다.")


# "http://127.0.0.1:8000/hello/
def hello(request):
    return HttpResponse("<h1>안녕하세요</h1>")
