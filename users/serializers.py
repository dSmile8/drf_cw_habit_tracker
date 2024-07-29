from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
    Этот класс отвечает за сериализацию экземпляров модели пользователя в формат JSON.

    Атрибуты:
    -----------
    model: users.models.User
        Класс модели Django, с которым связан этот сериализатор.
    fields: str
        Строка, представляющая поля, которые будут включены в сериализованный вывод.
        В этом случае «__all__» используется для включения всех полей.
    """

    class Meta:
        model = User
        fields = "__all__"
