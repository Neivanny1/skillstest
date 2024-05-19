from django.db import models
from django.contrib.auth.models import User

'''
All challenge models reside here
'''
class Participant(models.Model):
    '''
    Defines a class participants
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pic/participant", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=15, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
