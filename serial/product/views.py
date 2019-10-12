
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product
from .serializers import productSerializer
from rest_framework import status
# Create your views here.
@api_view(['GET','POST','DELETE'])
def getlist(request):

    if request.method=='GET':
       a=product.objects.all()
       serializer=productSerializer(a,many=True,write_only=True)
       
       return Response(serializer.data)

    elif request.method=='POST':
        serializer=productSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

    # elif request.method == 'DELETE':
    #     product.delete()
    #     return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getdetails(request,productName):
    try:
        abc = product.objects.get(productName=productName)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
       serializer=productSerializer(abc)
       return Response(serializer.data)

    elif request.method=='PUT':
        serializer=productSerializer(abc,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

    elif request.method == 'DELETE':
        serializer=productSerializer(abc)
        abc.delete()
        return Response(serializer.data)
        return Response(serializer.errors) 

    return HttpResponse(response, content_type='application/json')