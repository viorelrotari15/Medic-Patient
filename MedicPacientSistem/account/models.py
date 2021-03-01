from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('R', 'Receptionist'),
    ('MN', 'Manager')
]


class User(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=2)

    def is_doctor(self):
        if self.user_type == 'D':
            return True
        else:
            return False

    def is_patient(self):
        if self.user_type == 'P':
            return True
        else:
            return  False

    def is_receptionist(self):
        if self.user_type == 'R':
            return True
        else:
            return False

    def is_manager(self):
        if self.user_type == 'MN':
            return True
        else:
            return False

    class Meta:
        ordering = ('id',)



