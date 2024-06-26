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
    
    # profile_pic = models.ImageField(upload_to="profile_pic/participant", null=True, blank=True)
    address = models.CharField(max_length=60)
    email = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=20,null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
