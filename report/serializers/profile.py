from rest_framework import serializers
from report.choices import UserRoleChoices
from report.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class SingInProfileSerializers(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format='hex_verbose', read_only=True)
    name                = serializers.CharField(max_length=200, read_only=True)
    phone_no            = serializers.CharField(max_length=15, read_only=True)
    email_id            = serializers.EmailField()
    password            = serializers.CharField(max_length=128, write_only=True)
    role                = serializers.ChoiceField(choices=UserRoleChoices.choices, read_only=True)

    token               = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone_no',
            'email_id',
            'password',
            'role',
            'token'

        ]

    def get_token(self, instance: User):
        return instance.auth_token.key

    def validate(self, data):

        request = self.context.get("view").request

        #authenticate funciton 

        self.user = authenticate(request, email_id=data.get("email_id"), password=data.get("password"))

        if self.user is None:
            raise serializers.ValidationError("wrong email and passowrd entered")

        return data


    def create(self, validated_data):

                
        if hasattr(self.user, 'auth_token'):
                self.user.auth_token.delete()

        Token.objects.create(user=self.user)

        return self.user



