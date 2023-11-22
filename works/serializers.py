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


class CustomerSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=255)
    price_per_hour = serializers.DecimalField(max_digits=4, decimal_places=2)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class CreateCustomerSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=255)
    price_per_hour = serializers.DecimalField(max_digits=4, decimal_places=2)


class UpdateCustomerSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    address = serializers.CharField(max_length=255, required=False)
    price_per_hour = serializers.DecimalField(max_digits=4, decimal_places=2, required=False)


class LightPersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=200)


class WorkSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    employees = LightPersonSerializer(many=True)
    customer = LightPersonSerializer()
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
