import re
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'phone')

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Пароль повинен містити мінімум 8 символів"
            )
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Пароль повинен містити хоча б одну велику літеру"
            )
        if not re.search(r"\d", value):
            raise serializers.ValidationError(
                "Пароль повинен містити хоча б одну цифру"
            )
        return value

    def validate_phone(self, value):
        if not re.match(r'^\+380\d{9}$', value):
            raise serializers.ValidationError(
                "Телефон має бути у форматі +380XXXXXXXXX"
            )
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        return user
