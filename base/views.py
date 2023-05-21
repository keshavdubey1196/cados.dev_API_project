from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Company, UserModel
from .serializers import CompanySerializer, UserModelSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User

# RestFul conventions
"""
GET /advocates
POST /advocates

GET /advocates/:id
PUT /advocates/:id
DELETE /advocates/:id
"""


@api_view(["GET", "POST", "DELETE"])
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        name = request.data["name"]
        bio = request.data["bio"]

        obj = Company.objects.create(
            name=name,
            bio=bio
        )
        obj.save()
        serializer = CompanySerializer(obj, many=False)

        return Response(serializer.data)

    if request.method == "DELETE":
        company_id = request.data["company_id"]
        comp_obj = Company.objects.get(id=company_id)
        comp_obj.delete()

        return Response(status.HTTP_200_OK)


@api_view(["GET", "POST"])
def usersCreate(request):
    if request.method == "GET":
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        if UserModel.objects.filter(Q(email__icontains=request.data["email"])):
            return Response("This user already exists. If you want to update go to the patch link")
            # user = UserModel.objects.get(email=request.data["email"])
        else:
            serializer = UserModelSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.company.add(*request.data["company"])
                user.save()

                return Response(serializer.data)
            else:
                return Response(serializer.errors)


@api_view(["PATCH"])
def updateCompanyusers(request):
    if request.method == "PATCH":
        username = request.data["username"]
        email = request.data["email"]
        company_id = request.data["company"][0]

        if UserModel.objects.filter(username=username, email=email):
            user = UserModel.objects.get(username=username, email=email)
            company = Company.objects.get(id=company_id)
            company.users.add(user)

            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
