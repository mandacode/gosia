import typing as tp

from works.models import Customer


def list_customers() -> tp.List[Customer]:
    return Customer.objects.all()


def create_customer(
        *, first_name: str, last_name: str, phone_number: str, address: str, price_per_hour: float
) -> Customer:
    customer = Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
        price_per_hour=price_per_hour
    )
    return customer


def get_customer(customer_id: int) -> Customer:
    customer = Customer.objects.get(id=customer_id)
    return customer


def update_customer(
        *,
        customer_id: int,
        first_name: tp.Optional[str] = None,
        last_name: tp.Optional[str] = None,
        phone_number: tp.Optional[str] = None,
        address: tp.Optional[str] = None,
        price_per_hour: tp.Optional[float] = None,
) -> Customer:
    customer = Customer.objects.get(id=customer_id)

    if first_name:
        customer.first_name = first_name

    if last_name:
        customer.last_name = last_name

    if phone_number:
        customer.phone_number = phone_number

    if address:
        customer.address = address

    if price_per_hour:
        customer.price_per_hour = price_per_hour

    customer.save()

    return customer


def delete_customer(*, customer_id: int):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
