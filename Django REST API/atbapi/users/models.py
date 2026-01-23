<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='images/', blank=True, null=True)
    image_medium = models.ImageField(upload_to='images/', blank=True, null=True)
    image_large = models.ImageField(upload_to='images/', blank=True, null=True)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
<<<<<<< HEAD
        return self.email
=======
<<<<<<< HEAD
        return self.email
=======
<<<<<<< HEAD
        return self.email
=======
        return self.email
=======
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username
>>>>>>> 5f3157850eb87e28d70d2e6f1d58428d66ca0ed6
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
