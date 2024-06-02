from django.test import TestCase
from django.contrib.auth.models import User
from .models import Facilitator

class FacilitatorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='facilitator', password='12345', first_name='John', last_name='Doe')
        self.facilitator = Facilitator.objects.create(
            user=self.user,
            email='facilitator@example.com',
            profile_pic='profile_pic/facilitator/default.jpg',
            address='123 Main St',
            mobile='1234567890',
            status=False,
            salary=5000
        )

    def test_facilitator_creation(self):
        facilitator = Facilitator.objects.get(id=self.facilitator.id)
        self.assertEqual(facilitator.user.username, 'facilitator')
        self.assertEqual(facilitator.email, 'facilitator@example.com')
        self.assertEqual(facilitator.address, '123 Main St')
        self.assertEqual(facilitator.mobile, '1234567890')
        self.assertFalse(facilitator.status)
        self.assertEqual(facilitator.salary, 5000)

    def test_get_name(self):
        facilitator = Facilitator.objects.get(id=self.facilitator.id)
        self.assertEqual(facilitator.get_name, 'John Doe')

    def test_get_instance(self):
        facilitator = Facilitator.objects.get(id=self.facilitator.id)
        self.assertEqual(facilitator.get_instance, facilitator)

    def test_string_representation(self):
        facilitator = Facilitator.objects.get(id=self.facilitator.id)
        self.assertEqual(str(facilitator), 'John')
