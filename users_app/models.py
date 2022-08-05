from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(default='avatares/default.jpg',upload_to='avatares', null=True, blank=True)