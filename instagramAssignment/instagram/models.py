from django.db import models

# Create your models here.
class Post(models.Model):
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    #body = models.TextField(blank=True, null = True)
    image = models.ImageField(upload_to = "post/", blank = True, null = True)