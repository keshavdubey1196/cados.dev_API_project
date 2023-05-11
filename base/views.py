from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET'])
def advocates_list(request):
    advocates = Advocate.objects.all()
    serialzer = AdvocateSerializer(advocates, many=True)
    return Response(serialzer.data)


@api_view(['POST'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
