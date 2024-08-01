# Generated by Django 5.0.7 on 2024-08-01 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_remove_habit_related_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='related_habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка'),
        ),
    ]
