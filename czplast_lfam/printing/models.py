from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60)
    customer = models.CharField(max_length=60)
    image = models.ImageField(upload_to="projects/")
    date = models.DateField()
    material = models.CharField(max_length=60)
    printing_time = models.DurationField(null=True, blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.customer}"