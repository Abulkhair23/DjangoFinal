from django.db import models
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=30, blank=True, default="")
    phone = models.CharField(max_length=50, blank=True, default="")

#
# user = User.objects.get(id=1)
# user.is_staff = True
# user.save()
