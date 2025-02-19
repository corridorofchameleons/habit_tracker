import json

from rest_framework.test import APITestCase
from rest_framework.serializers import ValidationError
from habits.models import Habit
from users.models import User

from django.shortcuts import reverse
from rest_framework import status


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@kremlin.ru", password="qwertY87")
        self.habit = Habit.objects.create(
            time="9:00",
            duration=15,
            periodicity=3,
            action="пивко",
            is_public=True,
            place="диван",
            reward="чипсы",
            user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse('habits:habits')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('count'), 1
        )

    def test_habit_create(self):
        url = reverse('habits:habits')
        data = {
            "time": "9:00",
            "duration": 15,
            "periodicity": 3,
            "action": "Пивко",
            "is_public": True,
            "place": "Диван",
            "reward": "Сухарики",
            "user": self.user
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

        data = {
            "time": "9:00",
            "duration": 30,
            "periodicity": 3,
            "action": "Пивко",
            "is_public": True,
            "pleasant_habit": True,
            "place": "Диван",
            "reward": "Сухарики",
            "user": self.user
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
        data = {
            "time": "9:00",
            "duration": 300,
            "periodicity": 3,
            "action": "Пивко",
            "is_public": True,
            "place": "Диван",
            "reward": "Сухарики",
            "user": self.user
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_habit_update(self):
        url = reverse('habits:habit_update', args=(self.habit.pk,))
        data = {
            "action": "Кальян"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('action'), "Кальян"
        )

    def test_habit_delete(self):
        url = reverse('habits:habit_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_my_habits(self):
        url = reverse('habits:my_habits')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        print(data)
        self.assertEqual(
            data.get('count'), 1
        )
