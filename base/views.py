from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status


# RestFul conventions
"""
GET /advocates
POST /advocates

GET /advocates/:id
PUT /advocates/:id
DELETE /advocates/:id
"""


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
def advocates_list(request):
    # /advocates/?query=keshav
    if request.method == "GET":
        query = request.GET.get('query')

        if query is None:
            query = ''

        # For searching
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query))
        serialzer = AdvocateSerializer(advocates, many=True)
        return Response(serialzer.data)

    if request.method == "POST":
        # print(request.data)
        # return Response("done")

        adv = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio'],
        )
        serializer = AdvocateSerializer(adv, many=False)

        return Response(serializer.data)


class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()

        return Response("Advocate Deleted.")
