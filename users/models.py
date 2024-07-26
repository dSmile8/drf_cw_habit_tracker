from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    name = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона"
    )
    image = models.ImageField(
        upload_to="users/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите фото профиля"
    )
    city = models.CharField(
        verbose_name="город", **NULLABLE, help_text="Введите страну"
    )
    tg_chat_id = models.CharField(max_length=50, verbose_name='ID телеграмм чата')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
