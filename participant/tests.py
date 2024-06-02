from django.test import TestCase
from django.contrib.auth.models import User
from .models import Participant

class ParticipantModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', first_name='John', last_name='Doe')
        self.participant = Participant.objects.create(
            user=self.user,
            profile_pic='profile_pic/participant/default.jpg',
            address='123 Main St',
            email='test@example.com',
            mobile='1234567890'
        )

    def test_participant_creation(self):
        participant = Participant.objects.get(id=self.participant.id)
        self.assertEqual(participant.user.username, 'testuser')
        self.assertEqual(participant.address, '123 Main St')
        self.assertEqual(participant.email, 'test@example.com')
        self.assertEqual(participant.mobile, '1234567890')

    def test_get_name(self):
        participant = Participant.objects.get(id=self.participant.id)
        self.assertEqual(participant.get_name, 'John Doe')

    def test_get_instance(self):
        participant = Participant.objects.get(id=self.participant.id)
        self.assertEqual(participant.get_instance, participant)

    def test_string_representation(self):
        participant = Participant.objects.get(id=self.participant.id)
        self.assertEqual(str(participant), 'John')
