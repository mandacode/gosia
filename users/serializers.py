from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=6)
    street_address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)


class CreateEmployeeSerializer(CreateUserSerializer):

    nip = serializers.CharField(max_length=10)


class CreateCustomerSerializer(CreateUserSerializer):

    hourly_rate = serializers.DecimalField(max_digits=4, decimal_places=2)


class LightUserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class AddressSerializer(serializers.Serializer):

    zip_code = serializers.CharField(max_length=5)
    street_address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)


class CustomerProfileSerializer(serializers.Serializer):

    hourly_rate = serializers.DecimalField(max_digits=4, decimal_places=2)


class UserProfileSerializer(serializers.Serializer):

    address = AddressSerializer()
    is_customer = serializers.BooleanField()
    customer_profile = CustomerProfileSerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class EmployeeProfileSerializer(serializers.Serializer):

    nip = serializers.CharField(max_length=10)


class EmployeeUserProfileSerializer(serializers.Serializer):

    employee_profile = EmployeeProfileSerializer()
    address = AddressSerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class EmployeeSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    profile = EmployeeUserProfileSerializer()


class CustomerUserProfileSerializer(serializers.Serializer):

    customer_profile = CustomerProfileSerializer()
    address = AddressSerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class CustomerSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    profile = CustomerUserProfileSerializer()


class CreateOwnerSerializer(CreateUserSerializer):

    nip = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=255)
    phone_number_pl = serializers.CharField(max_length=255)
    phone_number_de = serializers.CharField(max_length=255)
    bank_name = serializers.CharField(max_length=255)
    iban = serializers.CharField(max_length=255)
    bic = serializers.CharField(max_length=255)
