from django.db import models
from django.db.models import Model
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True,null=True)
    featured_image = models.ImageField(blank=True,null=True, default='default.jpg')
    verse_text =models.CharField(max_length=200, blank=True,null=True) 
    verse_content =models.TextField( blank=True,null=True) 
    created = models.DateTimeField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.title

    
