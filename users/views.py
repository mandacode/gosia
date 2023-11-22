import logging

from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from .exceptions import UserAlreadyExists
from .serializers import CreateEmployeeSerializer, EmployeeSerializer, CreateCustomerSerializer, CustomerSerializer
from .services import create_employee, get_employees, create_customer, get_customers

logger = logging.getLogger(__name__)


class EmployeesAPIView(views.APIView):

    def post(self, request: Request) -> Response:
        input_serializer = CreateEmployeeSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            employee = create_employee(**input_serializer.validated_data)
        except UserAlreadyExists as exc:
            logger.error(exc.message)
            return Response(data={'error': exc.message}, status=status.HTTP_400_BAD_REQUEST)

        output_serializer = EmployeeSerializer(employee)
        logger.info("Create a new employee.")
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        employees = get_employees()

        serializer = EmployeeSerializer(employees, many=True)
        logger.info("List all employees.")
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CustomersAPIView(views.APIView):

    def post(self, request: Request) -> Response:
        input_serializer = CreateCustomerSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            customer = create_customer(**input_serializer.validated_data)
        except UserAlreadyExists as exc:
            logger.error(exc.message)
            return Response(data={'error': exc.message}, status=status.HTTP_400_BAD_REQUEST)

        output_serializer = CustomerSerializer(customer)
        logger.info("Create a new customer.")
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        customers = get_customers()

        serializer = CustomerSerializer(customers, many=True)
        logger.info("List all customers.")
        return Response(data=serializer.data, status=status.HTTP_200_OK)
