from django.db import models

# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(null=True)
    poll=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Voter(models.Model):
    name=models.CharField(max_length=200)
    adhar_number=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    

