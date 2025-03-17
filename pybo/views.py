from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from pybo.models import Question

# Create your views here.


# http://127.0.0.1:8000/pybo/
def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {"question_list": question_list}
    return render(request, "pybo/question_list.html", context)


# http://127.0.0.1:8000/pybo/<int:question_id>/
def detail(request, question_id):
    # question = Question.objects.filter(id=question_id)[0]
    # filter는 queryset을 반환하기 때문에 [0]을 붙여서 첫번째 데이터를 받아와야 한다.

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
