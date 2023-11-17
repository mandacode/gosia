from dataclasses import dataclass


@dataclass
class GosiaError(Exception):
    message: str
