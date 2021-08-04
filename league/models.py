from django.db import models
from django.utils import timezone
import time
# Create your models here.
class PlayerLogin(models.Model): #登录
    class Meta:
        verbose_name = 'PlayerLogin'
        verbose_name_plural = 'PlayerLogin' 
    mobile = models.CharField(max_length = 32 , unique=True)
    password = models.CharField(max_length = 64)
    def __str__(self):
        return PlayerInfo.objects.all().filter(player_login=self.id).first().player_name

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
    kit1_color = models.CharField(max_length = 32, default="ff0000")
    kit2_color = models.CharField(max_length = 32,default="0000ff")
    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    league_belong = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='League of this team')
    players = models.ManyToManyField("PlayerLogin",default=[])

    game_played = models.IntegerField(default=0)

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

class Match(models.Model): #比赛详情
    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
    match_time = models.DateTimeField('MatchTime',default = timezone.now)
    location = models.CharField(max_length = 64,default="", verbose_name='Location')
    is_gameover = models.BooleanField(default=False)

    home_team = models.ForeignKey(Team,related_name='hometeam', null=True,on_delete=models.SET_NULL, verbose_name='Home Team')
    away_team = models.ForeignKey(Team,related_name='awayteam', null=True,on_delete=models.SET_NULL, verbose_name='Away Team')

    home_team_kit_color = models.CharField(max_length = 32, default="ff0000")
    away_team_kit_color = models.CharField(max_length = 32,default="0000ff")

    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)

    match_round = models.IntegerField(default=0)
    match_number_this_round = models.IntegerField(default=0)
    match_number_this_league = models.IntegerField(default=0)

    remarks = models.CharField(max_length = 512,default="",blank=True)
    def __str__(self):
        return  "Game:" + str(self.id) + "->" + self.match_time.strftime("%Y-%m-%d %H:%M:%S") + " " + self.home_team.team_name + " VS " + self.away_team.team_name

    
