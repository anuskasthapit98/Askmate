from django.db import models
from django.core.validators import MinValueValidator

class UserModel (models.Model):
    name = models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    reputation= models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return(self.email)