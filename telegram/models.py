from django.db import models


STEP_CHOICES = (
    ("start", "Start"),
    ("ask_name", "Ask name"),
    ("ask_grade", "Ask grade"),
    ("ask_subject", "Ask subject"),
)


class BookGrades(models.Model):
    name = models.CharField(max_length=50)


class BookSubject(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    grade = models.ForeignKey(BookGrades, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(BookSubject, on_delete=models.SET_NULL, null=True, blank=True)

    def __str(self):
        return self.name

class TelegramUser(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, unique=True, blank=True)
    step = models.CharField(choices=STEP_CHOICES, max_length=100, default="start")
    favourite_subject = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)

    def __str__(self):
        return self.phone
