from rest_framework import serializers


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

