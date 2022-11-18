from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    #제목 최대 200개의 charField(글자갯수)
    content = models.TextField()
    # 질문내용은 텍스트필드 빈칸
    create_date = models.DateTimeField()
    # 질문 날짜는 시간필드
    def __str__(self):
        return self.subject
    #https://jamanbbo.tistory.com/11 str메서드
class Answer(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    # 포린키 안에 짝 지어져 있는 이유와. on delete 뜻?
    # Question을 속성으로 가져가기 위해 앞에 두고,
    # 뒤의 뜻은 Question 속성이 사라진다면 답변도 삭제된다.
    content = models.TextField()
    create_date = models.DateTimeField()

    