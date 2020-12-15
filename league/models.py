from django.db import models
from django.utils import timezone
# Create your models here.
class PlayerLogin(models.Model): #登录
    class Meta:
        verbose_name = 'PlayerLogin'
        verbose_name_plural = 'PlayerLogin' 
    mobile = models.CharField(max_length = 32 , unique=True)
    password = models.CharField(max_length = 64)
    def __str__(self):
        return self.mobile

class PlayerToken(models.Model): #token
    class Meta:
        verbose_name = 'PlayerToken'
        verbose_name_plural = 'PlayerToken' 
    user = models.OneToOneField(to='PlayerLogin', on_delete = models.CASCADE)
    token = models.CharField(max_length=64)
    def __str__(self):
        return self.user.mobile


class Role(models.Model): #角色
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles' 
    title = models.CharField(max_length = 32)
    def __str__(self):
        return self.title

class League(models.Model): #联赛
    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues' 
    league_name = models.CharField(max_length = 64)
    def __str__(self):
        return self.league_name

class Team(models.Model): #联赛中的队伍
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams' 

    team_name = models.CharField(max_length = 64,default="")
    kit1_color = models.CharField(max_length = 32, default="ffffff")
    kit2_color = models.CharField(max_length = 32,default="000000")
    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_aginst = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    league_belong = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='League of this team')
    players = models.ManyToManyField("PlayerLogin",default=[])

    def __str__(self):
        return self.team_name

class PlayerInfo(models.Model): #队员详情
    class Meta:
        verbose_name = 'PlayerDetail'
        verbose_name_plural = 'PlayerDetail'
    player_name = models.CharField(max_length = 64,default="Player")
    player_birthday = models.DateTimeField('Birthday',default = timezone.now)
    player_nation = models.CharField(max_length = 64,default="Player")

    player_login = models.OneToOneField(to='PlayerLogin', on_delete = models.CASCADE)
    player_roles = models.ManyToManyField("Role")
    player_league = models.ForeignKey(League,null=True,on_delete=models.SET_NULL, verbose_name='League of this player')
    player_team = models.ForeignKey(Team, null=True,on_delete=models.SET_NULL, verbose_name='Team of this player')
    def __str__(self):
        return self.player_name