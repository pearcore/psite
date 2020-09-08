from rest_framework import serializers
from app01 import models
class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"