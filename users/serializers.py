
from rest_framework import serializers

from users.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password':{'write_only':True}}

    def validate_password(self, value):
        if len(value) < 8:
            return serializers.ValidationError("The password must be greater than or equal to 8 characters.")
        return value


    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=True)
    password = serializers.CharField(max_length=128, write_only=True, allow_blank=True)




