# Create your views here.
import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Employee
from .services import (
    list_employees,
    create_employee,
    get_employee,
    update_employee,
    delete_employee
)
from employees.serializers import (
    EmployeeSerializer, CreateEmployeeSerializer, UpdateEmployeeSerializer
)

logger = logging.getLogger(__name__)


class EmployeesAPIView(APIView):

    def get(self, request: Request) -> Response:
        employees = list_employees()

        serializer = EmployeeSerializer(employees, many=True)
        logger.info("List all employees.")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        input_serializer = CreateEmployeeSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        employee = create_employee(**input_serializer.validated_data)

        output_serializer = EmployeeSerializer(employee)
        logger.info("Create new employee.")
        return Response(
            data=output_serializer.data, status=status.HTTP_201_CREATED
        )


class EmployeesDetailAPIView(APIView):

    def get(self, request: Request, employee_id: int) -> Response:
        try:
            employee = get_employee(employee_id)
        except Employee.DoesNotExist:
            data = {"error": "Employee not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        logger.info(f"Get employee | Id: {employee_id}")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, employee_id: int) -> Response:
        input_serializer = UpdateEmployeeSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            employee = update_employee(
                employee_id=employee_id, **input_serializer.validated_data
            )
        except Employee.DoesNotExist:
            data = {"error": "Employee not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        output_serializer = EmployeeSerializer(employee)
        logger.info(f"Update employee | Id: {employee_id}")
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, employee_id: int) -> Response:
        try:
            delete_employee(employee_id=employee_id)
        except Employee.DoesNotExist:
            data = {"error": "Employee not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"Delete employee | Id: {employee_id}")
        return Response(status=status.HTTP_204_NO_CONTENT)
