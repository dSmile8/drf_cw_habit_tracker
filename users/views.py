from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from users.models import User
from users.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    """
    Этот класс предоставляет конечную точку API для получения списка всех пользователей.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Этот класс предоставляет конечную точку API для получения информации о конкретном пользователе.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Этот класс предоставляет конечную точку API для создания нового пользователя.

    Атрибуты:
    queryset: набор запросов всех объектов User.
    serializer_class: класс сериализатора, который будет использоваться для сериализации и десериализации
    пользовательских данных.
    permission_classes: классы разрешений, которые будут применяться к этой конечной точке API.

    Методы:
    Perform_create(self, serializer): переопределенный метод для хэширования пароля пользователя перед его сохранением.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """
    Этот класс предоставляет конечную точку API для изменения информации о конкретном пользователе.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    """
    Этот класс предоставляет конечную точку API для удаления конкретного пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
