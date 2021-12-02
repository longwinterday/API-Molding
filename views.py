from django.db.models import QuerySet
from django.http import HttpRequest
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import ManufacturerSerializer, MoldingSerializer
from .models import Manufacturer, Molding
from .paginators import StandardResultPagination


class ManufacturerAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для отображения списка и создания экземпляров модели Производителя


    Methods:

    -------

    get_queryset() возвращает отфильтрованный список объектов модели

    get() метод обработки get-запросов

    post() метод обработки post-запросов
    """
    serializer_class = ManufacturerSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self) -> QuerySet[Manufacturer]:
        """
        Фильтрует список объектов класса Производитель при наличии имени Производителя в запросе
        :return: Отфильтрованный список экземпляров модели Производитель
        :rtype: Response
        """
        queryset = Manufacturer.objects.all()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title=title)
        return queryset

    def get(self, request: HttpRequest) -> Response:
        """
        Возвращает ответ со списком экземпляров класса Производитель в api-шаблон
        :param request: get-http-запрос
        :type: HttpRequest
        :return: отображение экземпляров модели в api-шаблон
        :rtype: Response
        """
        return self.list(request)

    def post(self, request: HttpRequest) -> Response:
        """
        Создаёт экземпляр класса Производитель
        :param request: post-http-запрос
        :type: HttpRequest
        :return: отображение экземпляров модели в api-шаблон
        :rtype: Response
        """
        return self.create(request)


class MoldingAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для отображения списка экземпляров класса модели Багета

    Methods:

    -------

    get_queryset() возвращает отфильтрованный список объектов модели

    get() метод обработки get-запросов
    """
    serializer_class = MoldingSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self) -> QuerySet[Molding]:
        """
        Фильтрует список объектов класса Багет по различным аргументам
        :return: Отфильтрованный список экземпляров модели Багет
        :rtype: Response
        """
        queryset = Molding.objects.all()
        manufacturer = self.request.query_params.get('manufacturer')
        title = self.request.query_params.get('title')
        price = self.request.query_params.get('price')
        filter_mark = self.request.query_params.get('filter')
        if manufacturer:
            queryset = queryset.filter(manufacturer__title=manufacturer)
        if title:
            queryset = queryset.filter(title=title)
        if price and filter_mark:
            if filter_mark == 'equal':
                queryset = queryset.filter(price=price)
            elif filter_mark == 'greater':
                queryset = queryset.filter(price__gte=price)
            elif filter_mark == 'lower':
                queryset = queryset.filter(price__lte=price)
        return queryset

    def get(self, request):
        """
        Возвращает ответ со списком экземпляров класса Багет в api-шаблон
        :param request: get-http-запрос
        :type: HttpRequest
        :return: отображение экземпляров модели в api-шаблон
        :rtype: Response
        """
        return self.list(request)

    def post(self, request):
        """
        Создаёт экземпляр класса Багет
        :param request: post-http-запрос
        :type: HttpRequest
        :return: отображение экземпляров модели в api-шаблон
        :rtype: Response
        """
        return self.create(request)
