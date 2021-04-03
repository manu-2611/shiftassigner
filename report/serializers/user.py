from rest_framework import serializers
from report.choices import UserRoleChoices
from report.models import User



class UserSerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format='hex_verbose')
    name                = serializers.CharField(max_length=200)
    phone_number        = serializers.CharField(max_length=15)
    email_id            = serializers.EmailField()
    password            = serializers.CharField(max_length=128, write_only=True)
    role                = serializers.ChoiceField(choices=UserRoleChoices.choices)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone_number',
            'email_id',
            'password',
            'role',

        ]

        
    def validate_id(self, value):
        if User.objects.filter(id=value).exists():
            
            raise serializers.ValidationError("You should enter a new Id,the user id is already registered")
        
        return value

    def validate_email_id(self, value):
        print("***********************************")
        if User.objects.filter(email_id=value).exists():
            raise serializers.ValidationError("You should enter a new Email Id, this emial_id is allready registered.")

        return value

    def create(self, validated_data):
        # print("*****************************")
        # print(**validated_data)
        return User.objects.create(**validated_data)

