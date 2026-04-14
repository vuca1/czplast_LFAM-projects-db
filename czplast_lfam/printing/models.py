from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60)
    customer = models.CharField(max_length=60)
    image = models.ImageField(upload_to="projects/")
    date = models.DateField()
    # TODO: material, printing time

    def __str__(self):
        return f"{self.name} - {self.customer}"