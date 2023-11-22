from rest_framework import serializers

from users.serializers import LightUserSerializer


class WorkSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    employees = LightUserSerializer(many=True)
    customer = LightUserSerializer()
    date = serializers.DateField()
    hours = serializers.DecimalField(required=False, max_digits=3, decimal_places=2)


class CreateWorkSerializer(serializers.Serializer):

    employee_ids = serializers.ListField(child=serializers.IntegerField())
    customer_id = serializers.IntegerField()
    date = serializers.DateField()
    hours = serializers.DecimalField(required=False, max_digits=3, decimal_places=2)


class UpdateWorkSerializer(serializers.Serializer):

    employee_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    customer_id = serializers.IntegerField(required=False)
    date = serializers.DateField(required=False)
    hours = serializers.DecimalField(required=False, max_digits=3, decimal_places=2)
