from django.db import models
from mongoengine import Document, StringField, ObjectIdField, IntField, PolygonField


class Providers(models.Model):
    """
        Providers Model
    """
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    language = models.CharField(max_length=50, blank=False)
    currency = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['id']


class Polygons(Document):
    """
        Polygon Model
    """

    _id = ObjectIdField()
    provider_id = IntField(blank=False)
    provider_name = StringField(max_length=50)
    name = StringField(max_length=50, blank=False)
    price = StringField(max_length=50, blank=False)
    geometry = PolygonField(blank=False)

    meta = {
        'db_alias': 'polygons-db',
    }
