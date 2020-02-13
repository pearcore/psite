from django.db import models
#→▸►☞⇢👉
class UserGroup(models.Model):
    class Meta:
        verbose_name = '用户分组'
        verbose_name_plural = '用户分组▸' 

    title = models.CharField(max_length=32,verbose_name='分组名称')
    
    def __str__(self):
        return self.title

class UserRole(models.Model):
    class Meta:
        verbose_name = '用户角色'
        verbose_name_plural = '用户角色▸' 

    title = models.CharField(max_length=32,verbose_name='角色名称')
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    class Meta:
        verbose_name = '用户详情'
        verbose_name_plural = '用户详情▸' 

    user_type_choices = (
        (1,'普通用户'),
        (2,'VIP用户'),
        (3,'SVIP用户'),
    )

    user_type = models.IntegerField(choices= user_type_choices)
    user_name = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

    group = models.ForeignKey("UserGroup" ,null = True, on_delete=models.CASCADE)
    role = models.ManyToManyField("UserRole")
    
    def __str__(self):
        return self.user_name

class UserToken(models.Model):
    class Meta:
        verbose_name = '用户token'
        verbose_name_plural = '用户token▸' 

    user = models.OneToOneField(to='UserInfo',on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.user.user_name
    
