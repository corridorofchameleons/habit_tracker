from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, MyHabitsListView

app_name = HabitsConfig.name

urlpatterns = [
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('', HabitListCreateAPIView.as_view(), name='habit_create'),
    path('my_habits/', MyHabitsListView.as_view(), name='my_habits'),
]
