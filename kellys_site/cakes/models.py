from django.db import models

class cakeRequest(models.Model):
    name = models.CharField(max_length=50)
    budget = models.CharField(max_length=200)
    request_date = models.DateTimeField('Date requested: ')
    
    def __str__(self):
        return self.name