from django.db import models

# Create your models here.

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django_countries.fields import CountryField

class UserBase(AbstractBaseUser, PerPermissionsMixin):
    email = models.EmailField(_('email address'), unique= True)
    user_name = models.CharField(max_length=255, unique =  True)
    first_name = models.CharField(max_length = 255, blank = True)
    about = models.TextField(_('about'), max_length = 500, blank = True)

    #Delivery details
    country = ContryField()
    phone_number = models.CharFields(max_length = 15, blank = True)
    postcode = models.CharFields(max_length = 12, blank = True)
    address_line_1 = models.CharFields(max_length = 150, blank = True)
    address_line_2 = models.CharFields(max_length = 150, blank = True)
    town_city = models.CharFields(max_length = 150, blank = True)

    #user Status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.user_name