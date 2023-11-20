from rest_framework import serializers


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


class ScratchpadSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    records = WorkSerializer(many=True)


class CreateScratchpadSerializer(serializers.Serializer):

    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, attrs: dict) -> dict:
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if start_date > end_date:
            raise serializers.ValidationError("Start date must be before end date.")

        return attrs


class UpdateScratchpadRecordSerializer(serializers.Serializer):

    hours = serializers.DecimalField(max_digits=3, decimal_places=2)

    def validate(self, attrs: dict) -> dict:
        hours = attrs.get("hours")

        if hours < 0:
            raise serializers.ValidationError("Hours must be greater than zero.")

        if float(hours) % 0.5:
            raise serializers.ValidationError("Hours must be a multiple of 0.5.")

        return attrs


class ScratchpadRecordSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    customer = LightPersonSerializer()
    employees = LightPersonSerializer(many=True)
    date = serializers.DateField()
    hours = serializers.DecimalField(max_digits=3, decimal_places=2)
