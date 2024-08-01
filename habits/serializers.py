from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import validate_duration, validate_periodicity


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[validate_duration])
    periodicity = serializers.IntegerField(validators=[validate_periodicity])

    class Meta:
        model = Habit
        exclude = ('user',)

    def validate(self, data):
        if data.get('related_habit') and data.get('reward'):
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и указать вознаграждение')
        if data.get('related_habit'):
            habit = Habit.objects.get(pk=data.get('related_habit').pk)
            if not habit.pleasant_habit:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                      'привычки')
        if data.get('pleasant_habit') and (data.get('related_habit') or data.get('reward')):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')

        return data
