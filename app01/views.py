import json
from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
def users(request):
    user_list = ["test01", "test02"]
    return HttpResponse( json.dumps(user_list))

class StudentsView(View):
    def get(self, request,*args, **kwargs):
        return HttpResponse("Get")

    def post(self, request,*args, **kwargs):
        return HttpResponse("Post")
