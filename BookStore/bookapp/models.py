from django.db import models

# Create your models here.

class Book(models.Model):
    '''
        Book Model
    '''
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date =  models.DateTimeField(auto_created=True)
    copies = models.IntegerField(null=True)
    rackno = models.IntegerField(null=True)
