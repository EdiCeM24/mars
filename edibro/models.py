from enum import Enum
from django.db import models
from django.db.utils import DatabaseError
from django.db import connection
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxValueValidator
from django.contrib.auth.models import User      # this is the default user model or a single user model
from django.contrib.auth import get_user_model   # this is the current user model
import uuid
from typing import FrozenSet, Set, Union
import warnings
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxValueValidator


class Contact(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True)
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True)
    email = models.EmailField(max_length=60, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?234?\d{9, 15}$', message="Phone number must be entered in the format: '+2348030999999'. Up to 15 digits is allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=15, blank=False)
    website = models.URLField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=100, validators=[MinLengthValidator(5), MaxValueValidator(100)])
    message = models.TextField(validators=[MinLengthValidator(3), MaxValueValidator(500)])

    def __str__(self):
        return self.first_name


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

CATEGORY_CHOICES = (
    ('Web Development', 'Web Development'),
    ('Mobile App Development', 'Mobile App Development'),
    ('Data Science', 'Data Science'),
    ('Machine Learning', 'Machine Learning'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Cybersecurity', 'Cybersecurity'),
    ('DevOps', 'DevOps'),
    ('UI/UX Design', 'UI/UX Design'),
    ('Game Development', 'Game Development'),
    ('Blockchain', 'Blockchain'),
    ('IoT', 'IoT'),
    ('Other', 'Other'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?234?\d{9, 15}$', message="Phone number must be entered in the format: '+2348030999999'. Up to 15 digits is allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images', blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username



class userTestimonial(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name    

class AppStrings:
    class AuthenticationMethod(str, Enum):
        USERNAME = "username"
        EMAIL = "email"
        USERNAME_EMAIL = "username_email"

    class LoginMethod(str, Enum):
        USERNAME = "username"
        EMAIL = "email"
        SOCIAL = "social"
        PHONE = "phone"

    class EmailVerificationMethod(str, Enum):
        MADATORY = "mandatory"
        OPTIONAL = "optional"
        NONE = "none"    
