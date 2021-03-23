from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField()
    bio = models.TextField()
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    professions = models.ForeignKey(models, on_delete=models.PROTECT)


class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(max_length=100)
