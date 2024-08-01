from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.pagination import MyPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = IsAuthenticated,
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = MyPaginator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = IsOwner,


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = IsOwner,


class MyHabitsListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = MyPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
