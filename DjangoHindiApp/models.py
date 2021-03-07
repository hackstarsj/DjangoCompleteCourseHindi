from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    notes_data=models.TextField()
    thumbnail=models.FileField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
