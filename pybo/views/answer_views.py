from urllib import response
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Answer, Question
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# dev_9
@login_required(login_url="common:login")  # dev_16
def answer_create(request, question_id):
    """
    pybo 답변등록
    """

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # dev_16 현재 로그인한 계정의 User 모델 객체
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id=question.id)

    else:
        return HttpResponseNotAllowed("Only POST is possible.")

    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)


# dev_18
@login_required(login_url="common:login")
def answer_modify(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect("pybo:detail", question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect("pybo:detail", question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)

    context = {"answer": answer, "form": form}
    return render(request, "pybo/answer_form.html", context)


# dev_18
@login_required(login_url="common:login")
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, "삭제권한이 없습니다")
    else:
        answer.delete()

    return redirect("pybo:detail", question_id=answer.question.id)


# dev_20
@login_required(login_url="common:login")
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할수 없습니다")
    else:
        answer.voter.add(request.user)
    return redirect("pybo:detail", question_id=answer.question.id)
