from rest_framework import serializers

from api.models import District, SubCounty


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = ('id', 'district_id', 'name')
