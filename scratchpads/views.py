import logging

from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import CreateScratchpadSerializer, ScratchpadSerializer, UpdateScratchpadRecordSerializer, \
    ScratchpadRecordSerializer
from .services import create_scratchpad, get_scratchpad, delete_scratchpad, update_scratchpad_record, \
    delete_scratchpad_record
from .models import Scratchpad, ScratchpadRecord

logger = logging.getLogger(__name__)


class ScratchpadAPIView(views.APIView):

    def post(self, request: Request) -> Response:
        input_serializer = CreateScratchpadSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        scratchpad = create_scratchpad(**input_serializer.validated_data)
        output_serializer = ScratchpadSerializer(scratchpad)
        logger.info(f"Create new scratchpad for date range: {request.data['start_date']} - {request.data['end_date']}.")
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class ScratchpadDetailAPIView(views.APIView):

    def get(self, request: Request, scratchpad_id: int) -> Response:
        try:
            scratchpad = get_scratchpad(scratchpad_id=scratchpad_id)
        except Scratchpad.DoesNotExist:
            data = {"error": "Scratchpad not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = ScratchpadSerializer(scratchpad)
        logger.info(f"Get scratchpad | Id: {scratchpad_id}")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, scratchpad_id: int) -> Response:
        try:
            delete_scratchpad(scratchpad_id=scratchpad_id)
        except Scratchpad.DoesNotExist:
            data = {"error": "Scratchpad not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"Delete scratchpad | Id: {scratchpad_id}")
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScratchpadDetailRecordsAPIView(views.APIView):

    def patch(self, request: Request, scratchpad_id: int, record_id: int) -> Response:
        input_serializer = UpdateScratchpadRecordSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            record = update_scratchpad_record(
                scratchpad_id=scratchpad_id,
                record_id=record_id,
                **input_serializer.validated_data
            )
        except Scratchpad.DoesNotExist:
            data = {"error": "Scratchpad not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        except ScratchpadRecord.DoesNotExist:
            data = {"error": "ScratchpadRecord not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        output_serializer = ScratchpadRecordSerializer(record)
        logger.info(f"Update scratchpad | Id: {scratchpad_id} | record: {record_id}.")
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, scratchpad_id: int, record_id: int) -> Response:

        try:
            delete_scratchpad_record(scratchpad_id=scratchpad_id, record_id=record_id)
        except Scratchpad.DoesNotExist:
            data = {"error": "Scratchpad not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        except ScratchpadRecord.DoesNotExist:
            data = {"error": "ScratchpadRecord not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"Delete scratchpad | Id: {scratchpad_id} | record: {record_id}.")
        return Response(status=status.HTTP_204_NO_CONTENT)
