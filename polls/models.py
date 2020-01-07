from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Question(models.Model):
    class Meta:
        verbose_name = '提问'
        verbose_name_plural = '提问' 

    question_text = models.CharField(max_length=200 , verbose_name='所提问题')
    pub_date = models.DateTimeField('发表时间')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项' 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='所属问题')
    choice_text = models.CharField(max_length=200, verbose_name='选项内容')
    votes = models.IntegerField(default=0, verbose_name='投票数')
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)