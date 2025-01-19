from django.db import models

def solution_upload_handler(instance, filename: str):
    ext = filename.split(".")[1]
    return f"{instance.name.lower()}-background.{ext}"

# Create your models here.
class Solution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    background = models.FileField(upload_to=solution_upload_handler, null=True, blank=True)

    def generate_slug(self):
        parts = self.name.split(" ")
        slug = "-".join(map(str.lower, parts))
        return slug
    
    @classmethod
    def get_name_from_slug(cls, slug: str):
        parts = slug.split("-")
        name = " ".join(map(lambda x: x.capitalize() if x not in ['and', 'or'] else x, parts))
        return name 
    
    @classmethod
    def get_instance_from_slug(cls, slug: str):
        return cls.objects.get(name=cls.get_name_from_slug(slug))


    def __str__(self):
        return f"{self.id} {self.name}"
    
