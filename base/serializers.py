from rest_framework.serializers import ModelSerializer
from base.models import Company, UserModel


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class CompanySerializer(ModelSerializer):
    # employee_count = SerializerMethodField(read_only=True)
    # employees = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    # def get_employee_count(self, obj):
    #     count = obj.advocate_set.count()
    #     return count
    # def get_employees(self, obj):
    #     employees = obj.advocate_set.all()
    #     return employees
