import datetime
import typing as tp

from django.contrib.auth.models import User

from works.models import Work
from works.exceptions import (
    WorkHasNoEmployees,
    WorkHasNoCustomer,
    WorkHasInvalidEmployee,
    WorkHasInvalidCustomer
)


def create_work(
        employee_ids: tp.List[int],
        customer_id: int,
        date: datetime.date,
        hours: int
) -> Work:

    employees = User.objects.filter(id__in=employee_ids)

    if employees.filter(profile__is_customer=True).count():
        raise WorkHasInvalidEmployee

    if not employees.count():
        raise WorkHasNoEmployees

    customer = User.objects.get(id=customer_id)

    if not customer.profile.is_customer:
        raise WorkHasInvalidCustomer

    work = Work.objects.create(
        customer=customer,
        date=date,
        hours=hours,
    )

    work.employees.add(*employees)

    return work


def list_works() -> tp.List[Work]:
    works = Work.objects.all()
    return works


def update_work(
        work_id: int,
        employee_ids: tp.Optional[tp.List[int]] = None,
        customer_id: tp.Optional[int] = None,
        date: tp.Optional[datetime.date] = None,
        hours: tp.Optional[int] = None
) -> Work:
    work = Work.objects.get(id=work_id)

    if employee_ids:
        employees = User.objects.filter(id__in=employee_ids)
        work.employees.set(employees)

    if customer_id:
        work.customer_id = customer_id

    if date:
        work.date = date

    if hours:
        work.hours = hours

    if not work.employees.count():
        raise WorkHasNoEmployees("Work must have at least one employee.")

    if not work.customer:
        raise WorkHasNoCustomer("Work must have a customer.")

    work.save()

    return work


def get_work(work_id: int) -> Work:
    work = Work.objects.get(id=work_id)
    return work


def delete_work(work_id: int):
    work = Work.objects.get(id=work_id)
    work.delete()

