import datetime
import typing as tp

from employees.models import Employee

from .exceptions import WorkHasNoEmployees, WorkHasNoCustomer
from .models import Work, ScratchpadRecord, Scratchpad


def create_work(
        employee_ids: tp.List[int],
        customer_id: int,
        date: datetime.date,
        hours: int
) -> Work:
    work = Work.objects.create(
        customer_id=customer_id,
        date=date,
        hours=hours,
    )
    work.employees.add(*employee_ids)
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
        employees = Employee.objects.filter(id__in=employee_ids)
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


def create_scratchpad(start_date: datetime.date, end_date: datetime.date) -> Scratchpad:
    works = Work.objects.filter(date__gte=start_date, date__lte=end_date)
    scratchpad = Scratchpad.objects.create(start_date=start_date, end_date=end_date)
    for work in works:
        scratchpad_record = ScratchpadRecord.objects.create(
            customer=work.customer,
            date=work.date,
            hours=work.hours,
        )
        scratchpad_record.employees.add(*work.employees.all())
        scratchpad.records.add(scratchpad_record)
    return scratchpad


def get_scratchpad(scratchpad_id: int) -> Scratchpad:
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    return scratchpad


def delete_scratchpad(scratchpad_id: int):
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    scratchpad.delete()


def update_scratchpad_record(scratchpad_id: int, record_id: int, hours: int) -> ScratchpadRecord:
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    record = scratchpad.records.get(id=record_id)
    record.hours = hours
    record.save()
    return record


def delete_scratchpad_record(scratchpad_id: int, record_id: int):
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    record = scratchpad.records.get(id=record_id)
    record.delete()
