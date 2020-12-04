from django.db import models
# Create your models here.
class PlayerLogin(models.Model):
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players' 
    mobile = models.CharField(max_length = 32 , unique=True)
    password = models.CharField(max_length = 64)
    def __str__(self):
        return self.mobile

class PlayerToken(models.Model):
    user = models.OneToOneField(to='PlayerLogin', on_delete = models.CASCADE)
    token = models.CharField(max_length=64)