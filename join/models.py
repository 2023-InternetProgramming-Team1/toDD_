from django.contrib.auth.models import AbstractUser
from eclass.models import Lecture
from django.db import models

class User(AbstractUser):
    studentId = models.IntegerField(unique=True)  # 학번 추가
    first_name = models.CharField(max_length=60)  # 하나의 이름으로 받기
    password = models.CharField(max_length=128)   # 비밀번호 추가
    lecture = models.ForeignKey(Lecture, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')  # related_name 추가

    USERNAME_FIELD = 'studentId'  # 이 부분을 추가하여 studentId를 로그인에 사용

    def __str__(self):
        return f"{self.first_name} - {self.studentId}"
