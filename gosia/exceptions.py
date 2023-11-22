import dataclasses


@dataclasses.dataclass
class GosiaError(Exception):
    message: str
