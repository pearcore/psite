from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class FinanceType(models.Model):
    class Meta:
        verbose_name = '记账类名'
        verbose_name_plural = '记账类名' 

    Name = models.CharField(max_length=200 , verbose_name='名称')
    CreateDate = models.DateTimeField('创建时间',default = timezone.now)
    def __str__(self):
        return self.Name

class FinanceRecord(models.Model):
    class Meta:
        verbose_name = '记账记录'
        verbose_name_plural = '记账记录' 

    FinanceType = models.ForeignKey(FinanceType, on_delete=models.CASCADE, verbose_name='记账类名')
    Reason = models.CharField(max_length=200 , verbose_name='是由')
    Amount = models.CharField(max_length=200 , verbose_name='数额')
    CreateDate = models.DateTimeField('记录时间',default = timezone.now)
    def __str__(self):
        return self.Reason