import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@csrf_exempt
def users(request):
    user_list = ["test01", "test02"]
    return HttpResponse( json.dumps(user_list))

from django.views import View

@method_decorator(csrf_exempt,name="dispatch")
class StudentsView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self , request, *args , **kwargs ):
    #     return super(StudentsView,self).dispatch(request, *args, **kwargs)

    def get(self, request,*args, **kwargs):
        return HttpResponse("Get")
    def post(self, request,*args, **kwargs):
        return HttpResponse("Post")
