from django.db import models

#class User(models.Model):
#    name = models.CharField(max_length=255)
#    email = models.EmailField(max_length=255, unique=True)


# Create your models here.
class Occurrence(models.Model):

    CATEGORY_CHOICES = (
        ('CONS_COND', 'CONSTRUCTION'),
        ('SPEC_COND', 'SPECIAL_EVENT'),
        ('INCI_COND', 'INCIDENT'),
        ('WTHR_COND', 'WEATHER_CONDITION'),
        ('ROAD_COND', 'ROAD_CONDITION')
    )

    author = models.CharField(max_length=100)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.PointField(null=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_upd = models.DateField(auto_now=True, verbose_name="date updated")
    status = models.CharField(max_length=100, default='not_validated')
    description = models.TextField(max_length=200, null=False, blank=False)


    category = models.CharField(
        max_length=9,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.author
