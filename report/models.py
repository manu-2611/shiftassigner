from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from report.choices import UserRoleChoices, WeekdaysChoices, RepeatFrequencyChoices, ShiftAavailability

class UserManager(BaseUserManager):
    def create(self, name, password, email_id, **kwargs):
        if not email_id:
            raise ValueError("email_id is required.")
        user = self.model(
            email_id = self.normalize_email(email_id),
            name = name,
            **kwargs
        )
        user.set_password(password)
        user.save(using=None)
        return user


class User(AbstractBaseUser):
    username            = None
    id                  = models.UUIDField(primary_key=True, editable=False)
    name                = models.CharField(max_length=200)
    phone_number        = PhoneNumberField()
    email_id            = models.EmailField(unique=True)
    role                = models.IntegerField(choices=UserRoleChoices.choices)

    objects = UserManager()

    USERNAME_FIELD ='email_id'
    REQUIRED_FIELDS = []


class Shift(models.Model):
    id                  = models.UUIDField(primary_key=True, editable=False)
    start_date          = models.DateField()
    arrival_time        = models.TimeField()
    departure_time      = models.TimeField()
    repeat              = models.IntegerField(choices=RepeatFrequencyChoices.choices)
    repeat_frequency    = models.IntegerField()
    shift_availability  = models.IntegerField(choices=ShiftAavailability.choices)
    weekdays            = models.IntegerField(choices=WeekdaysChoices.choices)
    client              = models.CharField(max_length=200)

# Create your models here.
