from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_reminder():

    for user in User.objects.all():
        message = 'Ваши планы:\n'
        for habit in user.habits.filter(pleasant_habit=False):
            time_left = timezone.now().date() - habit.started_at
            when = f'через {habit.periodicity - time_left.days} д.' if time_left.days else 'сегодня'
            message += f'{when} в {habit.time}: {habit.action}\n'
        send_telegram_message(user.telegram_id, message)
