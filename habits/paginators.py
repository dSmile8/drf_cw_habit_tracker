from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """
    Пользовательский класс нумерации страниц для конечных точек API, связанных с привычками.

    Этот класс наследуется от класса PageNumberPagination, предоставленного Django REST Framework.
    Он переопределяет настройки нумерации страниц по умолчанию для настройки поведения API.

    Атрибуты:
    page_size: количество элементов, отображаемых на странице. По умолчанию — 5.
    page_query_param: параметр запроса, используемый для указания номера страницы. По умолчанию — «page_size».
    max_page_size: максимальное количество элементов, разрешенное на странице. По умолчанию — 100.
    """

    page_size = 5
    page_query_param = "page_size"
    max_page_size = 100
