from rest_framework import serializers
from finance.models import FinanceType,FinanceRecord


class FinanceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceType
        fields = ('id', 'Name', 'CreateDate')

class FinanceRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceRecord
        fields = ('id', 'Reason', 'CreateDate','Amount','FinanceType')