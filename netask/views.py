from .models import Config
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vsite import LHKit
from .serializer import ConfigSerializer
from rest_framework import status

@api_view(['GET','POST'])
def rootAnswer(request):
    askName = request.POST.get('Name', '' )
    netask = get_object_or_404(Config, Name= askName)  # Config.objects.get(Name = 'ERCS')
    serializer = ConfigSerializer(netask, many=False)
    result = LHKit.LHStand.LHResult()
    result['data'] = serializer.data

    return Response(data=result, status=status.HTTP_200_OK)




