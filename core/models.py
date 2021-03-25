from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name="user")
    avatar = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Profession(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Worker(models.Model):
    profile = models.OneToOneField(Profile,primary_key=True, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField()
    bio = models.TextField(blank=True)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession)

    @property
    def ratings(self):
        return Review.objects.filter(reviewee=self)
    @property
    def rating_average(self):
        return sum([x.rating for x in self.ratings])/len(self.ratings)

    def __str__(self):
        return f'Worker {self.profile.user.username}'

class Review(models.Model):
    reviewer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True,null=True,related_name="reviewer")
    reviewee = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="reviewee")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.reviewee}'s review"
