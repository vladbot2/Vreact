<<<<<<< HEAD
from rest_framework import serializers
from .utils import compress_image
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'phone',
            'first_name', 
            'last_name', 
            'image_small', 
            'image_medium', 
            'image_large'
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True, required=False)  # лише одне поле для upload

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'image',
            'phone',
        ]

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        user = CustomUser.objects.create_user(
            **validated_data
        )

        if image:
            # створюємо 3 розміри
            optimized, name = compress_image(image, size=(300, 300))
            user.image_small.save(name, optimized, save=False)

            optimized, name = compress_image(image, size=(800, 800))
            user.image_medium.save(name, optimized, save=False)

            optimized, name = compress_image(image, size=(1200, 1200))
            user.image_large.save(name, optimized, save=False)

            user.save()

        return user
=======
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
>>>>>>> 5f3157850eb87e28d70d2e6f1d58428d66ca0ed6
