from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongo_serializer
from .models import Providers, Polygons


class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'language',
            'currency'
        ]


class PolygonsIncludesSerializer(mongo_serializer.DocumentSerializer):
    class Meta:
        model = Polygons
        fields = [
            '_id',
            'provider_name',
            'name',
            'price',
        ]


class PolygonsSerializer(mongo_serializer.DocumentSerializer):
    class Meta:
        model = Polygons
        fields = [
            '_id',
            'provider_id',
            'provider_name',
            'name',
            'price',
            'geometry'
        ]
