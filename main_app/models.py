from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length = 250)
    arena = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Player(models.Model):

    name = models.CharField(max_length=150)
    image = models.CharField(max_length=1000)
    position = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return self.name
    
