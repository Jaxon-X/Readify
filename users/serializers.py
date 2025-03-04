from rest_framework import serializers

from users.models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = "__all__"
        extra_kwargs = {'password':{'write_only':True}}

    def validate_password(self, value):
        if len(value) < 8:
            return serializers.ValidationError("The password must be greater than or equal to 8 characters.")
        return value


    def create(self, validated_data):
        user = CustomUserModel.objects.create_user(**validated_data)
        return user




