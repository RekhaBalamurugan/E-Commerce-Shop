# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)

    first_name = models.Field(blank=True)
    last_name = models.Field(blank=True)

    def __str__(self):
        return self.user.username
        

