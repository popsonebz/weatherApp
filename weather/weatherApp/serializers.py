from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Weather
        fields = ('date', 'min_temp', 'max_temp', 'wind', 'rain')
        #read_only_fields = ('date', 'min_temp', 'max_temp', 'wind', 'rain')