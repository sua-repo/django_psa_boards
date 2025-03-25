from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# dev_2
class Question(models.Model):
    # 필드가 null로 저장되는 것을 허용하려면 null=True 또는 blank=True를 설정

    # author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # dev_16
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )  # dev_16     # dev_20
    subject = models.CharField(max_length=100)
    content = models.TextField()  # 글자 수 제한 없는 텍스트는 TextField를 사용
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # dev_17     # 수정일시
    voter = models.ManyToManyField(
        User, related_name="voter_question"
    )  # dev_20  # 추천인 추가

    def __str__(self):
        return self.subject


# id (자동 생성) /
class Answer(models.Model):

    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # dev_16
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # dev_16

    # Question 모델과 1:N 관계 -> Question 모델이 삭제되면 답변도 함께 삭제
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # dev_17     # 수정일시


# Question.answer_set.all() => 역방향 참조 (O) / related_name="answers" => Question.answers.all()
# Answer.question => 정방향 참조 (O)
