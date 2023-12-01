from django.db import models
from django.contrib.auth.models import User

class review(models.Model):
    username=models.CharField(max_length=100)
    place=models.CharField(max_length=20)
    feedback=models.TextField()
    rating=models.DecimalField(decimal_places=1,max_digits=2)

class Booking(models.Model):
    class Passengers(models.IntegerChoices):
        ONE = 1, 'One passenger'
        TWO = 2, 'Two passengers'
        THREE = 3, 'Three passengers'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place=models.CharField(max_length=20)
    passengers=models.IntegerField(choices=Passengers.choices, default=Passengers.ONE)
    date = models.DateField()
    time = models.TimeField()
