from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


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
    data = ['/advocates', 'advocates/:username', 'company/']
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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


class AdvocateDetailView(APIView):
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


class CompanyListView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        # print(request.data)
        # return Response("successfull")
        company = Company.objects.create(
            name=request.data['name'],
            bio=request.data['bio'])
        serializer = CompanySerializer(company, many=False)

        return Response(serializer.data)
