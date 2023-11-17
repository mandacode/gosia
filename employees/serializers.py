from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class CreateEmployeeSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)


class UpdateEmployeeSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
