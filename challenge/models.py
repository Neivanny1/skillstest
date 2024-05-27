from django.db import models

from participant.models import Participant

class Speciality(models.Model):
   speciality_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.speciality_name

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

class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
def __str__(self):
    return self.participant.name