from django.db import models


# Create your models here.
class AidRequest(models.Model):
    id = models.AutoField(primary_key=True)
    brandname = models.CharField(max_length=30)
    message = models.TextField()
    donated_at = models.DateTimeField(auto_now_add=True)
    distributed = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.brandname} {self.donated_at}"
