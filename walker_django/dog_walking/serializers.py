from dynamic_rest import serializers, fields
from . import models


class PersonSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class DogSerializer(serializers.DynamicModelSerializer):
    walker = fields.DynamicRelationField('PersonSerializer', deferred=True)
    class Meta:
        model = models.Dog
        fields = '__all__'
