from rest_framework import serializers
from netask.models import Config


class ConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Config
        fields = ('id', 'Name', 'CreateDate', 'stResult','itResult','jsResult')