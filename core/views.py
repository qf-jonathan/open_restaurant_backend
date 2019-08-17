from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.safestring import mark_safe
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Ambient, Menu, Table, Order
from core.serializers import AmbientListSerializer, AmbientDetailSerializer, MenuSerializer, TableSerializer, \
    OrderSerializer
import json


class Index(View):
    def get(self, request, ambient_name):
        return render(request, 'core/index.html', {
            'room_name_json': mark_safe(json.dumps(ambient_name))
        })


class Kitchen(View):
    def get(self, request):
        return render(request, 'core/kitchen.html')


class AmbientViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Ambient.objects.all()
        serializer = AmbientListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Ambient.objects.prefetch_related('tables', 'tables__orders')
        ambient = get_object_or_404(queryset, pk=pk)
        serializer = AmbientDetailSerializer(ambient)
        return Response(serializer.data)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('menu', 'table')
    serializer_class = OrderSerializer
