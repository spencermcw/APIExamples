from django.shortcuts import render
from dynamic_rest import viewsets
from . import models
from . import serializers


class PersonViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class DogViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()
