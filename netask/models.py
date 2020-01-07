from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Config(models.Model):
    class Meta:
        verbose_name = '网上简询'
        verbose_name_plural = '网上简询' 

    Name = models.CharField(max_length=200 , verbose_name='简询名称')
    CreateDate = models.DateTimeField('创建时间',default = timezone.now)

    stResult = models.CharField('字符串应答',max_length=200, default='')
    itResult = models.IntegerField('整型应答', default= 0)
    jsResult = models.TextField('json应答',default='')
    def __str__(self):
        return self.Name