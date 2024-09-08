import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    birthday = models.DateTimeField("出生日期")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def __str__(self):
        return self.student_name

    def was_published_recently(self):
        return self.birthday >= timezone.now() - datetime.timedelta(days=1)


class Grade(models.Model):
    # 级联删除
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    subject = models.CharField(max_length=200)

    score = models.IntegerField(default=0)
