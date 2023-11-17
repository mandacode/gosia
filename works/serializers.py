from rest_framework import serializers


class LightPersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)


class WorkSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    employees = LightPersonSerializer(many=True)
    customer = LightPersonSerializer()
    date = serializers.DateField()
    hours = serializers.IntegerField()


class CreateWorkSerializer(serializers.Serializer):

    employee_ids = serializers.ListField(child=serializers.IntegerField())
    customer_id = serializers.IntegerField()
    date = serializers.DateField()
    hours = serializers.IntegerField()


class UpdateWorkSerializer(serializers.Serializer):

    employee_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    customer_id = serializers.IntegerField(required=False)
    date = serializers.DateField(required=False)
    hours = serializers.IntegerField(required=False)
