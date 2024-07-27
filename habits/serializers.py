from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelatedHabitValidator, DurationValidator, PleasantHabitValidator, RewardValidator,
                               PeriodicityValidator)
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Habit model.
    This serializer is used to convert Habit model instances into a format that can be easily transmitted and stored.
    It includes fields for all attributes of the Habit model, as well as a nested representation of the associated User.
    The class also includes a list of validators to enforce specific business rules related to the Habit model.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        """
        Meta class for the HabitSerializer.
        Defines the model and fields to be included in the serializer.
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
