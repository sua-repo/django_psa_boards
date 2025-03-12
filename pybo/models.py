from django.db import models


# Create your models here.
# dev_2
class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()  # 글자 수 제한 없는 텍스트는 TextField를 사용
    create_date = models.DateTimeField()


class Answer(models.Model):
    # Question 모델과 1:N 관계 -> Question 모델이 삭제되면 답변도 함께 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
