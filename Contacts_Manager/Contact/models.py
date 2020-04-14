from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=15, null = False, blank= False)
    Mobnum = models.IntegerField(primary_key=True)
    Company = models.CharField( max_length=15, null = False, blank= False)

    def __str__(self):
        return self.name