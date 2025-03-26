from urllib import response
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Answer, Question
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.


# dev_20    검색 추가
# http://127.0.0.1:8000/pybo
def index(request):

    # print(request.user)

    # ?page=4
    # ?kw=홍길동&page=1
    page = request.GET.get("page", "1")  # 페이지
    kw = request.GET.get("kw", "")  # 검색어

    question_list = Question.objects.order_by("-create_date")

    if kw:
        # SELECT * FROM question, user WHERE subject LIKE "%홍길동%"
        question_list = question_list.filter(
            Q(subject__contains=kw)  # 제목 검색
            | Q(content__icontains=kw)  # 내용 검색
            | Q(author__username__icontains=kw)  # 질문 글쓴이 검색
            | Q(answer__content__icontains=kw)  # 답변 내용 검색(역방향 참조)
            | Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색(역방향 참조)
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {"question_list": page_obj, "page": page, "kw": kw}

    return render(request, "pybo/question_list.html", context)


# http://127.0.0.1:8000/pybo/<int:question_id>/
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)

    # path(
    #     "answer/create/<int:question_id>/", views.answer_create, name="answer_create"
    # ),  # dev_5
