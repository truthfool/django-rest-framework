from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

# def ApiResponse(request):
    # data={
    #     'name':'Ishan',
    #     'age':22
    # } 

    # return JsonResponse(data,safe=False)

class ApiResponse(APIView):
    def get(self,request,*args,**kwargs):
        data={
        'name':'Ishan',
        'age':22
    }
        return Response(data)