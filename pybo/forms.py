from django import forms

from pybo.models import Answer, Question


# dev_9
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # form과 model을 연결
        fields = ["subject", "content"]  # QuestionForm에서 사용할 Question 모델의 속성


# dev_9
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # form과 model을 연결
        fields = [
            "content"
        ]  # question은 foreign key로 연결되어 있으므로 question은 제외하고 content만 입력받음
        labels = {"content": "답변내용"}  # 딕셔너리 형태
