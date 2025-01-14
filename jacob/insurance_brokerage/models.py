from django.db import models

# Create your models here.
class Cover(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    filename = models.CharField(max_length=255)
    description = models.TextField()

    @classmethod
    def slug_to_name(cls, slug:str):
        parts = slug.split("-")
        capitalized_parts = list(map(lambda x: x.capitalize(),parts))
        name = " ".join(capitalized_parts)
        return name 

    def name_to_slug(self):
        lowercased_name = self.name.lower()
        slugified_name = lowercased_name.replace(" ", "-")
        return slugified_name
    

    def __str__(self):
        return f"{self.id} {self.name}"

