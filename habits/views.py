from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitsListAPIView(ListAPIView):
    """
    Представление списка привычек, принадлежащих аутентифицированному пользователю.

    Атрибуты:
    - serializer_class: класс сериализатора, используемый для сериализации данных о привычках.
    - pagination_class: класс нумерации страниц, используемый для разбиения на страницы списка привычек.
    - permission_classes: классы разрешений, необходимых для доступа к этому представлению.
    """

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        возвращает набор запросов привычек, принадлежащих аутентифицированному пользователю.
        """

        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitsPublishedListAPIView(ListAPIView):
    """
    Представление списка опубликованных привычек.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемый для сериализации данных о привычках.
    - pagination_class: Класс нумерации страниц, используемый для разбиения на страницы списка привычек.
    """

    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        """
        Возвращает набор запросов опубликованных привычек.

        Возвращаемое значение:
        - QuerySet: Набор опубликованных привычек.
        """

        return Habit.objects.filter(is_published=True)


class HabitsCreateAPIView(CreateAPIView):
    """
    Представление для создания новой привычки.

    Атрибуты:
    - serializer_class: класс сериализатора, используемый для сериализации данных о привычках.
    - permission_classes: классы разрешений, необходимые для доступа к этому представлению.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Выполняет создание новой привычки.

        Параметры:
        - serializer (HabitSerializer): экземпляр сериализатора, содержащий проверенные данные о привычках.

        Возврат: None
        """

        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsRetrieveAPIView(RetrieveAPIView):
    """
     Представление для получения подробной информации о конкретной привычке.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемый для сериализации данных о привычках.
    - queryset: Набор объектов привычек, из которого выбирается конкретная привычка.
    - permission_classes: Классы разрешений, необходимые для доступа к этому представлению.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления информации о конкретной привычке.

    Атрибуты:
    - queryset: Набор объектов привычек, из которого выбирается конкретная привычка для обновления.
    - serializer_class: Класс сериализатора, используемый для сериализации и десериализации данных о привычках.
    - permission_classes: Классы разрешений, необходимые для доступа к этому представлению.
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления конкретной привычки.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемый для сериализации и десериализации данных о привычках.
    - queryset: Набор объектов привычек, из которого выбирается конкретная привычка для удаления.
    - permission_classes: Классы разрешений, необходимые для доступа к этому представлению.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
