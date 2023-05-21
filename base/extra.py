# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_details(request, username):
# advocate = Advocate.objects.get(username=username)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response("Advocate deleted")


# @api_view(['GET'])
# def endpoints(request):
#     data = ['/advocates', 'advocates/:username', 'company/']
#     return Response(data)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def advocates_list(request):
#     # /advocates/?query=keshav
#     if request.method == "GET":
#         query = request.GET.get('query')

#         if query is None:
#             query = ''

#         # For searching
#         advocates = Advocate.objects.filter(
#             Q(username__icontains=query) | Q(bio__icontains=query))
#         serialzer = AdvocateSerializer(advocates, many=True)
#         return Response(serialzer.data)

#     if request.method == "POST":
#         # print(request.data)
#         # return Response("done")

#         adv = Advocate.objects.create(
#             username=request.data['username'],
#             bio=request.data['bio'],
#         )
#         serializer = AdvocateSerializer(adv, many=False)

#         return Response(serializer.data)


# class AdvocateDetailView(APIView):
#     def get_object(self, username):
#         try:
#             return Advocate.objects.get(username=username)
#         except Advocate.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, username):
#         advocate = self.get_object(username)
#         serializer = AdvocateSerializer(advocate, many=False)

#         return Response(serializer.data)

#     def put(self, request, username):
#         advocate = self.get_object(username)

#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     def delete(self, request, username):
#         advocate = self.get_object(username)
#         advocate.delete()

#         return Response("Advocate Deleted.")


# class CompanyListView(APIView):
#     def get(self, request):
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)

#         return Response(serializer.data)

#     def post(self, request):
#         # print(request.data)
#         # return Response("successfull")
#         company = Company.objects.create(
#             name=request.data['name'],
#             bio=request.data['bio'])
#         serializer = CompanySerializer(company, many=False)

#         return Response(serializer.data)


# @api_view(["PATCH"])
# def updateUser(request, username):
#     instance = UserModel.objects.get(username=username)
#     serializer = UserModelSerializer(
#         instance, data=request.data, partial=True, many=True)

#     if serializer.is_valid():
#         # serializer.save()
#         instance.company.add(*serializer.validated_data["company"])
#         instance.save()

#         print(instance.company.all())

#         return Response("success")

"""
@api_view(["PATCH"])
def updateCompanyusers(request):
    if request.method == "PATCH":
        username = request.data["username"]
        email = request.data["email"]
        company_id = request.data["company"][0]
        if username and email and company_id:
            print(username, email, company_id)
            if UserModel.objects.filter(username=username, email=email):
                user = UserModel.objects.get(username=username, email=email)
                company = Company.objects.get(id=company_id)

                company.users.add(user)

                return Response(status.HTTP_200_OK)

            else:
                return Response(status.HTTP_404_NOT_FOUND)
        else:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)"""

"""
@api_view(["PATCH"])
def updateCompanyusers(request):
    if request.method == "PATCH":
        username = request.data["username"]
        email = request.data["email"]
        company_id = request.data["company"]

        if UserModel.objects.filter(username=username, email=email):
            for pk in company_id:
                user = UserModel.objects.get(username=username, email=email)
                company = Company.objects.get(id=pk)
                company.users.add(user)

            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)"""
