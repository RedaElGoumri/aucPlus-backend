from rest_framework import serializers
from .models import Enchere

class EnchereSerializer(serializers.ModelSerializer):
    class Meta:
            model = Enchere
            fields = ('id', 'name', 'description', 'typelot', 'typevente', 'responsable')