import dataclasses

from gosia.exceptions import GosiaError


@dataclasses.dataclass
class WorkHasNoEmployees(GosiaError):
    message: str = "Work must have at least one employee."


@dataclasses.dataclass
class WorkHasNoCustomer(GosiaError):
    message: str = "Work must have a customer."


@dataclasses.dataclass
class WorkHasInvalidEmployee(GosiaError):
    message: str = "Work cannot have a customer as an employee."


@dataclasses.dataclass
class WorkHasInvalidCustomer(GosiaError):
    message: str = "Work cannot have an employee as a customer."
