from django.test import TestCase
from django.contrib.auth.models import User
from participant.models import Participant
from .models import Speciality, Question, Result

class SpecialityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.speciality = Speciality.objects.create(
            speciality_name='Mathematics',
            question_number=10,
            total_marks=100,
            time_limit=60,
            free_or_paid=Speciality.FREE,
            owner_name='John Doe',
            owner_id=self.user
        )

    def test_speciality_creation(self):
        speciality = Speciality.objects.get(id=self.speciality.id)
        self.assertEqual(speciality.speciality_name, 'Mathematics')
        self.assertEqual(speciality.free_or_paid, Speciality.FREE)
        self.assertEqual(speciality.owner_name, 'John Doe')
        self.assertEqual(speciality.owner_id.username, 'testuser')

class QuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.speciality = Speciality.objects.create(
            speciality_name='Science',
            question_number=15,
            total_marks=150,
            time_limit=75,
            free_or_paid=Speciality.PAID,
            owner_name='Jane Doe',
            owner_id=self.user
        )
        self.question = Question.objects.create(
            speciality=self.speciality,
            marks=10,
            question='What is the boiling point of water?',
            option1='90°C',
            option2='100°C',
            option3='110°C',
            option4='120°C',
            answer='Option2'
        )

    def test_question_creation(self):
        question = Question.objects.get(id=self.question.id)
        self.assertEqual(question.question, 'What is the boiling point of water?')
        self.assertEqual(question.answer, 'Option2')
        self.assertEqual(question.speciality.speciality_name, 'Science')

class ResultModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.participant = Participant.objects.create(
            user=self.user,
            address='123 Main St',
            email='test@example.com',
            mobile='1234567890'
        )
        self.speciality = Speciality.objects.create(
            speciality_name='History',
            question_number=20,
            total_marks=200,
            time_limit=90,
            free_or_paid=Speciality.FREE,
            owner_name='Jack Smith',
            owner_id=self.user
        )
        self.result = Result.objects.create(
            participant=self.participant,
            speciality=self.speciality,
            marks=95
        )

    def test_result_creation(self):
        result = Result.objects.get(id=self.result.id)
        self.assertEqual(result.marks, 95)
        self.assertEqual(result.participant.user.username, 'testuser')
        self.assertEqual(result.speciality.speciality_name, 'History')
