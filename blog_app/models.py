from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
	    ordering = ['-date']



