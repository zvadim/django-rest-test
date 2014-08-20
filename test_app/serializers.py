from rest_framework import serializers
from cities.models import PostalCode


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = ('code', 'region_name')