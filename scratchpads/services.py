import datetime
import typing as tp

from works.models import Work
from .models import Scratchpad, ScratchpadRecord


def get_scratchpads() -> tp.List[Scratchpad]:
    scratchpads = Scratchpad.objects.all()
    return scratchpads


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


def update_scratchpad_record(scratchpad_id: int, record_id: int, hours: tp.Optional[int] = None) -> ScratchpadRecord:
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    record = scratchpad.records.get(id=record_id)
    if hours:
        record.hours = hours
    record.save()
    return record


def delete_scratchpad_record(scratchpad_id: int, record_id: int):
    scratchpad = Scratchpad.objects.get(id=scratchpad_id)
    record = scratchpad.records.get(id=record_id)
    record.delete()
