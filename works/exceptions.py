from gosia.exceptions import GosiaError


class WorkHasNoEmployees(GosiaError):
    message = "Work must have at least one employee."


class WorkHasNoCustomer(GosiaError):
    message = "Work must have a customer."
