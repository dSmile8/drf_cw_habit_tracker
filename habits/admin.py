from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """
    Пользовательский интерфейс администратора для модели Habit.

    Этот класс обеспечивает настройки интерфейса администратора Django.
    например: указание полей для отображения в виде списка,
    параметры фильтрации и поля поиска.

    Атрибуты:
    - list_display: кортеж имен полей для отображения в виде списка.
    - list_filter: кортеж имен полей, которые будут использоваться в качестве фильтров в представлении списка.
    - search_fields: кортеж имен полей, которые будут использоваться для поиска в представлении списка.
    """
    list_display = (
        "owner",
        "action",
        "is_published",
    )
    list_filter = ("owner",)
    search_fields = ("action",)