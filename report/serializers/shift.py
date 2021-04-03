from rest_framework import serializers
from report.choices import WeekdaysChoices, RepeatFrequencyChoices
from report.models import Shift



class ShiftSerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format='hex_verbose')
    start_date          = serializers.DateField()
    arrival_time        = serializers.TimeField()
    departure_time      = serializers.TimeField()
    repeat              = serializers.ChoiceField(choices=RepeatFrequencyChoices.choices)
    repeat_frequency    = serializers.IntegerField()
    shift_availability  = serializers.BooleanField()
    weekdays            = serializers.ChoiceField(choices=WeekdaysChoices.choices)
    # client              = serializers.CharField(max_length=200)

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
            "weekdays"


        ]

        
    def validate_id(self, value):
        if not self.instance and Shift.objects.filter(id=value).exists():
            
            raise serializers.ValidationError("You should enter a new Id,the user id is already registered")
        
        return value


    def create(self, validated_data):

        client = self.context.get("view").request.user
        print(client)

        user: User = Shift.objects.create(**validated_data, client=client)

        return user
