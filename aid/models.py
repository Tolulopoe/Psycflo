from django.db import models

# Create your models here.
class Aid(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=40)
    message=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=20)
    phonenumber=models.CharField()


    def __str__(self):
        return f"{self.fullname} {self.submitted_at}"
    

