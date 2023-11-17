import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Customer
from .services import (
    list_customers,
    create_customer,
    get_customer,
    update_customer,
    delete_customer
)
from .serializers import (
    CustomerSerializer,
    CreateCustomerSerializer,
    UpdateCustomerSerializer
)

logger = logging.getLogger(__name__)


class CustomersAPIView(APIView):

    def get(self, request: Request) -> Response:
        employees = list_customers()

        serializer = CustomerSerializer(employees, many=True)
        logger.info("List all customers.")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        input_serializer = CreateCustomerSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        customer = create_customer(**input_serializer.validated_data)

        output_serializer = CustomerSerializer(customer)
        logger.info("Create new customer.")
        return Response(
            data=output_serializer.data, status=status.HTTP_201_CREATED
        )


class CustomersDetailAPIView(APIView):

    def get(self, request: Request, customer_id: int) -> Response:
        try:
            customer = get_customer(customer_id)
        except Customer.DoesNotExist:
            data = {"error": "Customer not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        logger.info(f"Get customer | Id: {customer_id}")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, customer_id: int) -> Response:
        input_serializer = UpdateCustomerSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            customer = update_customer(
                customer_id=customer_id, **input_serializer.validated_data
            )
        except Customer.DoesNotExist:
            data = {"error": "Customer not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        output_serializer = CustomerSerializer(customer)
        logger.info(f"Update customer | Id: {customer_id}")
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, customer_id: int) -> Response:
        try:
            delete_customer(customer_id=customer_id)
        except Customer.DoesNotExist:
            data = {"error": "Customer not found."}
            logger.error(data["error"])
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"Delete customer | Id: {customer_id}")
        return Response(status=status.HTTP_204_NO_CONTENT)
