from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.geos import Point
#from django.contrib.postgres.fields import HStoreField
#from django.db.models import Manager as GeoManager


class Occurrence(models.Model):
    """Create database."""

    CATEGORY_CHOICES = (
        ('CONS_COND', 'CONSTRUCTION'),
        ('SPEC_COND', 'SPECIAL_EVENT'),
        ('INCI_COND', 'INCIDENT'),
        ('WTHR_COND', 'WEATHER_CONDITION'),
        ('ROAD_COND', 'ROAD_CONDITION')
    )

    STATUS_CHOICES = (
        ('not_validated', 'not_validated'),
        ('validated', 'validated'),
        ('solved', 'solved')
    )
    author = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    #location = models.PointField(srid=4326)
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_upd = models.DateField(auto_now=True, verbose_name="date updated")
    status = models.CharField(choices=STATUS_CHOICES, max_length=13, default='not_validated')
    description = models.TextField(max_length=200, null=False, blank=False)


    category = models.CharField(
        max_length=9,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.author
