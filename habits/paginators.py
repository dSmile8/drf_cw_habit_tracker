from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """
    Custom pagination class for habit-related API endpoints.

    This class inherits from the PageNumberPagination class provided by Django REST Framework.
    It overrides the default pagination settings to customize the behavior of the API.

    Attributes:
    page_size: The number of items to display per page. Default is 5.
    page_query_param: The query parameter used to specify the page number. Default is "page_size".
    max_page_size: The maximum number of items allowed per page. Default is 100.
    """

    page_size = 5
    page_query_param = "page_size"
    max_page_size = 100
