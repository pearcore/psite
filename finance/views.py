from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from vsite import LHKit
from .models import FinanceType,FinanceRecord
from .serializer import FinanceTypeSerializer,FinanceRecordSerializer

@api_view(['POST'])
def typelist(request, format=None):
    ftypes = FinanceType.objects.all().order_by('-CreateDate')
    itCount = len(ftypes)
    page = int ( request.POST.get('page',1 ) )
    rows = int ( request.POST.get('rows', 5  ) )
   
    standRt = LHKit.LHStand.LHResult()
    if (page-1)*rows > itCount :
        standRt ['data'] = []
    else :
        lastPageNumber = rows
        if  ((page * rows) >= itCount ) :
            lastPageNumber = itCount - ((page - 1) * rows)
        ser = FinanceTypeSerializer(instance=ftypes[(page-1)*rows: (page-1)*rows + lastPageNumber] , many=True)
        standRt['data'] = ser.data
    return Response(data=standRt, status=status.HTTP_200_OK)

@api_view(['POST'])
def typeadd(request,format=None):
    name = str ( request.POST.get('Name','') )

    obj =  FinanceType.objects.create(Name = name )
    standRt = LHKit.LHStand.LHResult()
    standRt['data'] = FinanceTypeSerializer(obj,many=False).data
    standRt["msg"] = "添加成功!"
    return Response(data = standRt ,  status=status.HTTP_200_OK)

@api_view(['POST'])
def typedel(request, format=None):
   itID = int ( request.POST.get('id',0 ) )
   ftypes = FinanceType.objects.get(pk=itID).delete();
    
   standRt = LHKit.LHStand.LHResult()
   standRt["msg"] = "删除成功了!"
   return Response(data=standRt, status=status.HTTP_200_OK)

@api_view(['POST'])
def recordlist(request, format=None):
    page = int ( request.POST.get('page',1) )
    rows = int ( request.POST.get('rows',5) )
    financeType = str ( request.POST.get('financeType',0) )
    records = FinanceRecord.objects.filter( FinanceType=financeType ).order_by('-CreateDate')
    itCount = len(records)
   
    standRt = LHKit.LHStand.LHResult()
    if (page-1)*rows > itCount :
        standRt ['data'] = []
    else :
        lastPageNumber = rows
        if  ((page * rows) >= itCount ) :
            lastPageNumber = itCount - ((page - 1) * rows)
        ser = FinanceRecordSerializer(instance=records[(page-1)*rows: (page-1)*rows + lastPageNumber] , many=True)
        standRt['data'] = ser.data
    return Response(data=standRt, status=status.HTTP_200_OK)

@api_view(['POST'])
def recordadd(request,format=None):
    reason = str ( request.POST.get('Reason','') )
    amount = str ( request.POST.get('Amount','') )
    itType = int ( request.POST.get('FinanceType',0) )
    f = FinanceType.objects.get(id = itType)
    obj =  FinanceRecord.objects.create(Reason = reason , Amount = amount, FinanceType = f)
    r = FinanceRecordSerializer(instance=obj , many = False)
    print (r)
    standRt = LHKit.LHStand.LHResult()
    standRt['data'] = r.data
    standRt["msg"] = "添加成功!"
    return Response(data = standRt ,  status=status.HTTP_200_OK)

@api_view(['POST'])
def recorddel(request, format=None):
   itID = int ( request.POST.get('id',0 ) )
   ftypes = FinanceRecord.objects.get(pk=itID).delete();
    
   standRt = LHKit.LHStand.LHResult()
   standRt['msg'] = "删除成功了!"
   return Response(data=standRt, status=status.HTTP_200_OK)

@api_view(['POST'])
def recordclean(request, format=None):
    itType = int ( request.POST.get('fid',0 ) )
    f = FinanceType.objects.get(id = itType)
    records = FinanceRecord.objects.filter(FinanceType = f)
    blance = 0.0
    for temp in records:
        blance += float ( temp.Amount )
    FinanceRecord.objects.filter(FinanceType= f).delete()
    FinanceRecord.objects.create(Reason = '结余' , Amount = round ( blance, 2) , FinanceType = f)
    standRt = LHKit.LHStand.LHResult()
    standRt["msg"] = "清理成功!"
    standRt["data"] = blance
    return Response(data=standRt, status=status.HTTP_200_OK)




