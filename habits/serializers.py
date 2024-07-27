from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelatedHabitValidator, DurationValidator, PleasantHabitValidator, RewardValidator,
                               PeriodicityValidator)
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.
    Этот сериализатор используется для преобразования экземпляров модели Habit в формат, который можно легко передавать
    и сохранять.
    Он включает поля для всех атрибутов модели привычки, а также вложенное представление связанного пользователя.
    Класс также включает список валидаторов для обеспечения соблюдения определенных правил,
    связанных с моделью привычки.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        """
        Мета-класс для HabitSerializer.
        Определяет модель и поля, которые будут включены в сериализатор.
        """

        model = Habit
        fields = "__all__"
        validators = [
            RelatedHabitValidator("related_habit", "reward"),
            DurationValidator("duration"),
            PleasantHabitValidator("related_habit", "pleasant_habit_sign"),
            RewardValidator("reward", "related_habit", "pleasant_habit_sign"),
            PeriodicityValidator("periodicity"),
        ]
