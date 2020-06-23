from django.shortcuts import render,HttpResponse
import json
from psite.LHStand import LHKit
# Create your views here.
def users(request):
    user_list = ["Test","dkdkdk"]
    rt = LHKit.LHResult()
    rt['data'] = user_list
    return HttpResponse( json.dumps( rt ) )

from django.views import View

class StudentsView(View):
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