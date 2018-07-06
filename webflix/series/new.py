from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=true)
	name = serializers.CharField()
	realease_date = serializers.DateField()
