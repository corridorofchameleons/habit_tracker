from rest_framework.exceptions import ValidationError


def validate_time(time):
    if not 1 < time <= 120:
        raise ValidationError('Время выполнения не должно превышать 120 сек')
