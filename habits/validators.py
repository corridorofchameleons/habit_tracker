from rest_framework.exceptions import ValidationError


def validate_duration(duration):
    '''
    Валидация продолжительности
    '''
    if not 1 < duration <= 120:
        raise ValidationError('Время выполнения не должно превышать 120 сек')


def validate_periodicity(periodicity):
    '''
    Валидация периодичности
    '''
    if periodicity > 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
