from django.db import models
# Create your models here.
class PlayerLogin(models.Model):
    class Meta:
        verbose_name = 'PlayerLogin'
        verbose_name_plural = 'PlayerLogin' 
    mobile = models.CharField(max_length = 32 , unique=True)
    password = models.CharField(max_length = 64)
    def __str__(self):
        return self.mobile

class PlayerToken(models.Model):
    class Meta:
        verbose_name = 'PlayerToken'
        verbose_name_plural = 'PlayerToken' 
    user = models.OneToOneField(to='PlayerLogin', on_delete = models.CASCADE)
    token = models.CharField(max_length=64)
    def __str__(self):
        return self.user.mobile

class League(models.Model):
    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues' 
    league_name = models.CharField(max_length = 64)
    def __str__(self):
        return self.league_name

class Club(models.Model):
    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs' 
    club_name = models.CharField(max_length = 64,default="")

    kit1_color = models.CharField(max_length = 32, default="ffffff")
    kit2_color = models.CharField(max_length = 32,default="000000")

    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    
    goals_for = models.IntegerField(default=0)
    goals_aginst = models.IntegerField(default=0)

    points = models.IntegerField(default=0)
    
    league_belong = models.ManyToManyField('League')
    players = models.ManyToManyField("PlayerLogin",)
    
    def __str__(self):
        return self.club_name