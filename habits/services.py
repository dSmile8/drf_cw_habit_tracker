import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(tg_chat_id, message):
    """
    Отправляет сообщение в указанный чат Telegram с помощью API Telegram Bot.

    Параметры:
    tg_chat_id (int): уникальный идентификатор целевого чата.
    message (str): Текст сообщения, которое будет отправлено.

    Возврат: None
    """
    params = {
        "text": message,
        "chat_id": tg_chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)