from django.core.exceptions import ValidationError


def validateNonASCII(value):
    if not value.isascii():
        raise ValidationError("Only ASCII characters are allowed")
    return value

def validateNonNegativeAndNotZero(value):
    if value <= 0:
        raise ValidationError("Only non-negative values are allowed")
    return value