from django.db import models
class UserGroup(models.Model):
    title = models.CharField(max_length = 32)

class UserInfo(models.Model):
    user_type_choices = (
        (1,'普通用户'),
        (2,'VIP用户'),
        (3,'VIP中P用户'),
    )
    user_type = models.IntegerField(choices = user_type_choices)
    username = models.CharField(max_length = 32 , unique=True)
    password = models.CharField(max_length = 64)

    group = models.ForeignKey("UserGroup", null = True , on_delete= models.CASCADE)
    roles = models.ManyToManyField("Role")

class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete = models.CASCADE)
    token = models.CharField(max_length=64)

class Role(models.Model):
    title = models.CharField(max_length = 32)

from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

class Course(models.Model):
    title = models.CharField(max_length = 32)
    price_policy_list = GenericRelation("PricePolicy")

class DegreeCourse(models.Model):
    title = models.CharField(max_length = 32)
    price_policy_list = GenericRelation("PricePolicy")
    
class PricePolicy(models.Model):
    price = models.IntegerField()
    period = models.IntegerField()

    content_type = models.ForeignKey(ContentType ,verbose_name='关联的表名称',on_delete= models.CASCADE)
    object_id = models.IntegerField(verbose_name='关联的表的数据行的ID')
    content_object = GenericForeignKey('content_type','object_id')
