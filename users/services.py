import typing as tp

from django.contrib.auth.models import User

from .models import UserProfile, Address, CustomerProfile, EmployeeProfile
from .exceptions import UserAlreadyExists


def create_user(first_name: str, last_name: str) -> User:
    username = f"{first_name}.{last_name}".lower()

    if User.objects.filter(username=username).exists():
        raise UserAlreadyExists(f"User {first_name} {last_name} ({username}) already exists.")

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
    )
    return user


def create_address(
        zip_code: str,
        street_address: str,
        city: str,
        country: str,
) -> Address:
    address = Address.objects.create(
        zip_code=zip_code,
        street_address=street_address,
        city=city,
        country=country,
    )
    return address


def create_employee(
        first_name: str,
        last_name: str,
        zip_code: str,
        street_address: str,
        city: str,
        country: str,
        nip: str,
) -> User:
    user = create_user(first_name=first_name, last_name=last_name)

    address = create_address(
        zip_code=zip_code,
        street_address=street_address,
        city=city,
        country=country,
    )

    employee_profile = EmployeeProfile.objects.create(
        nip=nip,
    )

    UserProfile.objects.create(
        user=user,
        address=address,
        employee_profile=employee_profile,
    )

    return user


def create_customer(
        first_name: str,
        last_name: str,
        zip_code: str,
        street_address: str,
        city: str,
        country: str,
        hourly_rate: float,
) -> User:
    user = create_user(first_name=first_name, last_name=last_name)

    address = create_address(
        zip_code=zip_code,
        street_address=street_address,
        city=city,
        country=country
    )

    customer_profile = CustomerProfile.objects.create(
        hourly_rate=hourly_rate,
    )

    UserProfile.objects.create(
        user=user,
        address=address,
        is_customer=True,
        customer_profile=customer_profile,
    )

    return user


def get_employees() -> tp.List[User]:
    employees = User.objects.filter(
        profile__is_customer=False,
        profile__customer_profile__isnull=True,
        profile__employee_profile__isnull=False
    )
    return employees


def get_customers() -> tp.List[User]:
    customers = User.objects.filter(
        profile__is_customer=True,
        profile__employee_profile__isnull=True,
        profile__customer_profile__isnull=False
    )
    return customers
