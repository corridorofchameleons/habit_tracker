from django.db import models


class Habit(models.Model):
    '''
    Модель привычки
    '''

    user = models.ForeignKey('users.User', related_name='habits', on_delete=models.CASCADE, verbose_name='Пользователь')

    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    periodicity = models.SmallIntegerField(verbose_name='Периодичность')
    action = models.CharField(max_length=100, verbose_name='Действие')

    pleasant_habit = models.BooleanField(verbose_name='Полезная привычка', default=False)
    related_habit = models.BooleanField(verbose_name='Приятная привычка', null=True)
    reward = models.CharField(verbose_name='Вознаграждение', null=True)

    is_public = models.BooleanField(verbose_name='Видно всем')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
