from django.shortcuts import render#导入render模块
 
#先定义一个数据列表，当然后面熟了可以从数据库里取出来
 
def index(request):
 
    return render(request,'index2.html')