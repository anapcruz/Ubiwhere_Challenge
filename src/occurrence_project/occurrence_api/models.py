from django.db import models

# Create your models here.
class Occurrence(models.Model):
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='por_validar')
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.author