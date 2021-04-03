from rest_framework import serializers
from report.choices import WeekdaysChoices, RepeatFrequencyChoices
from report.models import Shift



class ShiftListSerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format='hex_verbose')
    start_date          = serializers.DateField()
    arrival_time        = serializers.TimeField()
    departure_time      = serializers.TimeField()
    repeat              = serializers.ChoiceField(choices=RepeatFrequencyChoices.choices)
    repeat_frequency    = serializers.IntegerField()
    shift_availability  = serializers.BooleanField()
    weekdays            = serializers.ChoiceField(choices=WeekdaysChoices.choices)
    client              = serializers.CharField(max_length=200)

    class Meta:
        model = Shift
        fields = [
            "id",
            "start_date",
            "arrival_time",
            "departure_time",
            "repeat",
            "repeat_frequency",
            "shift_availability",
            "weekdays",
            "client"


        ]

