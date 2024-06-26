from django.db import models
from participant.models import Participant
from django.contrib.auth.models import User


'''
Class that defines a table in db to stored challenges uploaded
'''
class Speciality(models.Model):
    FREE = 0
    PAID = 1
    FREE_OR_PAID_CHOICES = [
        (FREE, 'Free'),
        (PAID, 'Paid'),
    ]
    speciality_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    free_or_paid = models.PositiveIntegerField(choices=FREE_OR_PAID_CHOICES, default=FREE)
    amount = models.PositiveIntegerField(null=True, blank=True)
    owner_name = models.CharField(max_length=200)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.speciality_name

'''
Class that defines a table in db to stored questions uploaded
'''
class Question(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    marks =models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3','Option3'), ('Option4', 'Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    def __str__(self):
        return f"Question: {self.question}, Marks: {self.marks}, Options: [{self.option1}, {self.option2}, {self.option3}, {self.option4}], Answer: {self.answer}"


'''
Class that defines a table in db to stored scores for participants
'''
class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
def __str__(self):
    return self.participant.name