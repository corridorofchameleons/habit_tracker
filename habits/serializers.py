from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_time


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        validators = {
            'time': validate_time,
        }
        exclude = ('user',)
