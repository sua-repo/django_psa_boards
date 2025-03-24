from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from pybo.form import AnswerForm, QuestionForm
from pybo.models import Answer
from pybo.models import Question
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


# http://127.0.0.1:8000/pybo/
def index(request):
    page = request.GET.get("page", "1")  # 페이지

    question_list = Question.objects.order_by("-create_date")

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # context = {"question_list": question_list}
    context = {"question_list": page_obj}

    return render(request, "pybo/question_list.html", context)


# http://127.0.0.1:8000/pybo/<int:question_id>/
def detail(request, question_id):
    # question = Question.objects.filter(id=question_id)[0]
    # filter는 queryset을 반환하기 때문에 [0]을 붙여서 첫번째 데이터를 받아와야 한다.

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)


# path(
#        "answer/create/<int:question_id>/", views.answer_create, name="answer_create"
#    ),  # dev_5


# dev_5 / dev_9 / dev_16
@login_required(login_url="common:login")
def answer_create(request, question_id):

    # request.user = AnonymousUser()    # dev_16

    # dev_9
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # dev_16
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id=question.id)

        else:
            form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)


# dev_9 / dev_16
# path("question/create/", views.question_create, name="question_create"),  # dev_9
@login_required(login_url="common:login")
def question_create(request):

    print(request.POST.get("content"))

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # dev_16
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")

    else:
        form = QuestionForm()
        return render(request, "pybo/question_form.html", {"form": form})

    return render(request, "pybo/question_form.html", {"form": form})
