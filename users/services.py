import typing as tp

from django.contrib.auth.models import User

from .models import UserProfile, Address, CustomerProfile, EmployeeProfile, UserType, OwnerProfile, \
    BankAccount
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

    user_profile = UserProfile.objects.create(
        user=user,
        address=address,
        type=UserType.EMPLOYEE
    )

    EmployeeProfile.objects.create(
        nip=nip,
        user_profile=user_profile,
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

    user_profile = UserProfile.objects.create(
        user=user,
        address=address,
        type=UserType.CUSTOMER,
    )

    CustomerProfile.objects.create(
        hourly_rate=hourly_rate,
        user_profile=user_profile,
    )

    return user


def create_owner(
        first_name: str,
        last_name: str,
        zip_code: str,
        street_address: str,
        city: str,
        country: str,
        email: str,
        phone_number: str,
        bank_name: str,
        iban: str,
        bic: str,
        nip: str,
        ust_idnr: str
) -> User:
    user = create_user(first_name=first_name, last_name=last_name)

    address = create_address(
        zip_code=zip_code,
        street_address=street_address,
        city=city,
        country=country
    )

    user_profile = UserProfile.objects.create(
        user=user,
        address=address,
        type=UserType.OWNER,
    )

    bank_account = BankAccount.objects.create(
        bank_name=bank_name,
        iban=iban,
        bic=bic,
    )

    OwnerProfile.objects.create(
        user_profile=user_profile,
        email=email,
        phone_number=phone_number,
        ust_idnr=ust_idnr,
        bank_account=bank_account,
        nip=nip,
    )

    return user


def get_employees() -> tp.List[User]:
    employees = User.objects.filter(
        profile__customer_profile__isnull=True,
        profile__employee_profile__isnull=False,
        profile__owner_profile__isnull=True
    )
    return employees


def get_customers() -> tp.List[User]:
    customers = User.objects.filter(
        profile__customer_profile__isnull=False,
        profile__employee_profile__isnull=True,
        profile__owner_profile__isnull=True
    )
    return customers


def get_owner() -> User:
    owner = User.objects.get(
        profile__employee_profile__isnull=True,
        profile__customer_profile__isnull=True,
        profile__owner_profile__isnull=False
    )
    return owner
