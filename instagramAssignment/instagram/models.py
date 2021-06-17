from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(CustomUser, related_name="posts", on_delete=CASCADE)
    pub_date = models.DateTimeField()
    #body = models.TextField(blank=True, null = True)
    image = models.ImageField(upload_to = "post/", blank = True, null = True)