from django.db import models
from django.db.utils import DatabaseError
from django.db import connection
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxValueValidator
from django.contrib.auth.models import User      # this is the default user model or a single user model
from django.contrib.auth import get_user_model   # this is the current user model
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxValueValidator

class Contact(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True)
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9, 18}$', message="Phone number must be entered in the format: '+234 803 099 9999'. Up to 15 digits is allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=15, blank=False)
    website = models.URLField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=50, validators=[MinLengthValidator(5), MaxValueValidator(50)])
    message = models.TextField(validators=[MinLengthValidator(3), MaxValueValidator(300)])

    def __str__(self):
        return self.first_name


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"


class Product(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    



class userTestimonial(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

