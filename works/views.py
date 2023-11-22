import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import (
    WorkSerializer,
    CreateWorkSerializer,
    UpdateWorkSerializer,
    CustomerSerializer,
    CreateCustomerSerializer,
    UpdateCustomerSerializer,
    EmployeeSerializer,
    CreateEmployeeSerializer,
    UpdateEmployeeSerializer
)

from .services.works import (
    list_works,
    create_work,
    update_work,
    delete_work,
    get_work
)
from .services.customers import (
    update_customer,
    list_customers,
    create_customer,
    get_customer,
    delete_customer,
)
from .services.employees import (
    list_employees,
    create_employee,
    get_employee,
    update_employee,
    delete_employee
)
from .models import Work, Customer, Employee

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

# TODO FLOW: create works -> create scratchpad -> update scratchpad -> create bill -> print bill
