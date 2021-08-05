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