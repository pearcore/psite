from django.contrib import admin
from .models import FinanceType,FinanceRecord

admin.site.register(FinanceType)
admin.site.register(FinanceRecord)