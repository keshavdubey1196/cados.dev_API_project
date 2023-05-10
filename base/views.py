# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET'])
def advocates_list(request):
    data = ['Dennis', 'keshav', 'Myself']
    return JsonResponse(data, safe=False)


@api_view(['POST'])
def advocate_details(request, username):
    data = username
    return JsonResponse(data, safe=False)
