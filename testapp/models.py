from django.db import models

# Create your models here.

class  Test(models.Model):
    test_id = models.IntegerField()
    description= models.CharField(max_length=200)




