from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidence(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
    objects = GeoManager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '1. Incidences'
        
class County(models.Model):
    county = models.CharField(max_length=20)
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField() 
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


    def __str__(self):
        return self.county
    
    class Meta:
        verbose_name_plural = '2. Counties'