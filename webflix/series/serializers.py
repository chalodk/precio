from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Serie
		fields = ('id', 'name', 'release_date', 'rating', 'category')

#	pk = serializers.IntegerField(read_only=True)
#	name = serializers.CharField()
#	release_date = serializers.DateField()
#	rating = serializers.IntegerField()
#	category = serializers.ChoiceField(choices=Serie.CATEGORIES_CHOICES)
#
#	def create(self, validated_data):
#		return Serie.objects.create(**validated_data)
#
#	def update(self, instance, validated_data):
#		instance.name = validated_data.get('name', instance.name)
#		instance.release_date = validated_data.get('release_date', instance.release)
#		instance.rating = validated_data.get('rating', instance.rating)
#		instance.category = validated_data.get('category', instance.category)
#		instance.save()
#		return instance

