from django.shortcuts import render

from rest_framework.views import APIView
from tools.LHStand import LHKit
#from rest_framework.response import Response
from django.http import JsonResponse 

# Create your views here.


class TestView(APIView): 
   def get(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        ret['data'] = '喔靠'
        return JsonResponse(ret)