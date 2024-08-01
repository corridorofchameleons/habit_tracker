from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('', HabitCreateAPIView.as_view(), name='habit_create'),
]
