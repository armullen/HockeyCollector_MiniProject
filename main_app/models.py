from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length = 250)
    arena = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']