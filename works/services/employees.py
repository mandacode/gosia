import typing as tp

from works.models import Employee


def list_employees() -> tp.List[Employee]:
    return Employee.objects.all()


def create_employee(*, first_name: str, last_name: str, phone_number: str) -> Employee:
    employee = Employee.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
    )
    return employee


def get_employee(employee_id: int) -> Employee:
    employee = Employee.objects.get(id=employee_id)
    return employee


def update_employee(
        *,
        employee_id: int,
        first_name: tp.Optional[str] = None,
        last_name: tp.Optional[str] = None,
        phone_number: tp.Optional[str] = None
) -> Employee:
    employee = Employee.objects.get(id=employee_id)

    if first_name:
        employee.first_name = first_name

    if last_name:
        employee.last_name = last_name

    if phone_number:
        employee.phone_number = phone_number

    employee.save()

    return employee


def delete_employee(*, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
