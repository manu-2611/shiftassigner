from typing import Dict, List

from django.db import models

class UserRoleChoices(models.IntegerChoices):
    CLIENT = 1


class RepeatFrequencyChoices(models.IntegerChoices):
    DAILY   =   1
    MONTHLY =   2
    YEARLY  =   3


class WeekdaysChoices(models.IntegerChoices):
    MONDAY      =   1
    TUESDAY     =   2
    WEDNESDAY   =   3
    THURSDAY    =   4
    FRIDAY      =   5
    SATURDAY    =   6
    SUNDAY      =   7


class ShiftAavailability(models.IntegerChoices):
    MORNING_SHIFT_5AM_TO_9AM    =   1
    