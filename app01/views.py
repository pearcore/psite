from django.shortcuts import render,HttpResponse
import json
from psite.LHStand import LHKit
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.

def users(request):
    user_list = ["Test","dkdkdk"]
    rt = LHKit.LHResult()
    rt['data'] = user_list
    return HttpResponse( json.dumps( rt ) )

from django.views import View

class StudentsView(View):
    #@method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):
        print('before')
        ret = super(StudentsView,self).dispatch(request , *args , **kwargs)
        print('after')
        return ret 
    
    def get(self,request , *args, **kwargs):
        user_list = ["dddd","aaaaa"]
        rt = LHKit.LHResult()
        rt['data'] = user_list
        return HttpResponse( json.dumps( rt ) )
    def post(self,request , *args, **kwargs):
        user_list = ["Post","Post"]
        rt = LHKit.LHResult()
        rt['data'] = user_list
        return HttpResponse( json.dumps( rt ) )
    def put(self,request , *args, **kwargs):
        user_list = ["Method","这个是PUT方法"]
        rt = LHKit.LHResult()
        rt['data'] = user_list
        return HttpResponse( json.dumps( rt ,ensure_ascii=False) )

    def delete(self,request , *args, **kwargs):
        user_list = {"Method":"delete"}
        rt = LHKit.LHResult()
        rt['data'] = user_list
        return HttpResponse( json.dumps( rt ) )