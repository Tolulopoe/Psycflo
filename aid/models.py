from django.db import models




class AidRequest(models.Model):
 fullname = models.CharField(max_length=255)
 email = models.CharField(max_length=255)
 state = models.CharField(max_length=255)
 country = models.CharField(max_length=255)
 localgovernment= models.CharField(max_length=255)
 phoneno= models.IntegerField()


