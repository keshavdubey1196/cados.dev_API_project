from rest_framework.serializers import ModelSerializer, SerializerMethodField
from base.models import Advocate, Company


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    # employees = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count
    # def get_employees(self, obj):
    #     employees = obj.advocate_set.all()
    #     return employees


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Advocate
        fields = ['id', 'username', 'bio', 'company']
