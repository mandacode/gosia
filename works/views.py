import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import (
    WorkSerializer,
    CreateWorkSerializer,
    UpdateWorkSerializer,
    ScratchpadSerializer,
    CreateScratchpadSerializer,
    ScratchpadRecordSerializer, UpdateScratchpadRecordSerializer
)
from .services import (
    list_works,
    create_work,
    update_work,
    delete_work,
    get_work,
    get_scratchpad,
    create_scratchpad,
    update_scratchpad_record,
    delete_scratchpad_record,
    delete_scratchpad,
)
from .models import Work, Scratchpad, ScratchpadRecord

logger = logging.getLogger(__name__)


class WorksAPIView(APIView):

    def get(self, request: Request) -> Response:
        works = list_works()

        serializer = WorkSerializer(works, many=True)
        logger.info("List all works.")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        input_serializer = CreateWorkSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        work = create_work(**input_serializer.validated_data)

        output_serializer = WorkSerializer(work)
        logger.info("Create new work.")
        return Response(
            data=output_serializer.data, status=status.HTTP_201_CREATED
        )


class WorksDetailAPIView(APIView):

    def get(self, request: Request, work_id: int) -> Response:
        try:
            work = get_work(work_id=work_id)
        except Work.DoesNotExist:
            data = {"error": "Work not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkSerializer(work)
        logger.info(f"Get work | Id: {work_id}")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, work_id: int) -> Response:
        input_serializer = UpdateWorkSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            work = update_work(
                work_id=work_id, **input_serializer.validated_data
            )
        except Work.DoesNotExist:
            data = {"error": "Work not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        output_serializer = WorkSerializer(work)
        logger.info(f"Update work | Id: {work_id}")
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, work_id: int) -> Response:
        try:
            delete_work(work_id=work_id)
        except Work.DoesNotExist:
            data = {"error": "Work not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"Delete work | Id: {work_id}")
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScratchpadAPIView(APIView):

    def post(self, request: Request) -> Response:
        input_serializer = CreateScratchpadSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        scratchpad = create_scratchpad(**input_serializer.validated_data)
        output_serializer = ScratchpadSerializer(scratchpad)
        logger.info(f"Create new scratchpad for date range: {request.data['start_date']} - {request.data['end_date']}.")
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class ScratchpadDetailAPIView(APIView):

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


class ScratchpadDetailRecordsAPIView(APIView):

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

# TODO move scratchpad to new app, move employees/customers to works app
# TODO -> /works/employees/1
# TODO -> /works/customers/1
# TODO -> /scratchpads/1
# TODO -> /scratchpads/1/records/1
# TODO -> /bills -> POST {start_date, end_date, type, recipient_id}
# TODO -> /bills/1 -> GET
# TODO -> /bills/1/print/ -> POST
# TODO -> /bills/print/ -> POST

# TODO FLOW: create works -> create scratchpad -> update scratchpad -> create bill -> print bill
