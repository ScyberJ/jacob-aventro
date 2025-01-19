from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} ({self.email})"
