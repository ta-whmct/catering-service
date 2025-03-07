from enum import StrEnum, unique

from app.domain.exception import ValueErrorEnumException


class ValueObjectEnum(StrEnum):
    @classmethod
    def from_value(cls, value: str) -> "ValueObjectEnum":
        try:
            return ValueObjectEnum(value)
        except ValueError:
            raise ValueErrorEnumException()


@unique
class OrderState(ValueObjectEnum):
    created = "created"
    aknownledged = "aknowledge"
    activated = "activated"
    completed = "completed"
    cancelled = "cancelled"
