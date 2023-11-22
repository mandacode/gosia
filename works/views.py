import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from gosia.exceptions import GosiaError
from .serializers import (
    WorkSerializer,
    CreateWorkSerializer,
    UpdateWorkSerializer,
)

from .services import (
    list_works,
    create_work,
    update_work,
    delete_work,
    get_work
)
from .models import Work

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

        try:
            work = create_work(**input_serializer.validated_data)
        except GosiaError as error:
            logger.error(error.message)
            return Response(data={'detail': error.message}, status=status.HTTP_400_BAD_REQUEST)

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


# TODO move scratchpad to new app, move employees/customers to works app
# TODO -> /works/employees/1
# TODO -> /works/customers/1
# TODO -> /scratchpads/1
# TODO -> /scratchpads/1/records/1
# TODO -> /bills -> POST {start_date, end_date, type, recipient_id}
# TODO -> /bills/1 -> GET
# TODO -> /bills/1/print/ -> POST
# TODO -> /bills/print/ -> POST

# TODO /users/:
# employee_profile
# customer_profile
# is_customer
# TODO create head profile

# TODO FLOW: create works -> create scratchpad -> update scratchpad -> create bill -> print bill
