from rest_framework import serializers

from users.serializers import LightUserSerializer
from works.serializers import WorkSerializer


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

    hours = serializers.DecimalField(max_digits=3, decimal_places=2, required=False)

    def validate(self, attrs: dict) -> dict:
        hours = attrs.get("hours")

        if not hours:
            return attrs

        if hours < 0:
            raise serializers.ValidationError("Hours must be greater than zero.")

        if float(hours) % 0.5:
            raise serializers.ValidationError("Hours must be a multiple of 0.5.")

        return attrs


class ScratchpadRecordSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    customer = LightUserSerializer()
    employees = LightUserSerializer(many=True)
    date = serializers.DateField()
    hours = serializers.DecimalField(max_digits=3, decimal_places=2)
