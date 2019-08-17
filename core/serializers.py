from rest_framework import serializers
from core.models import Ambient, Menu, Table, Order


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'label', 'active']


class AmbientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambient
        fields = ['id', 'name', 'active']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'menu', 'table', 'state', 'detail', 'requested_at', 'dispatched_at']


class TableDetailSerializer(serializers.ModelSerializer):
    orders = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ['id', 'label', 'active', 'orders']


class AmbientDetailSerializer(serializers.ModelSerializer):
    tables = TableDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Ambient
        fields = ['id', 'name', 'active', 'tables']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'active']


class OrderSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    table = TableSerializer(read_only=True)
    dispatched_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'menu', 'table', 'state', 'detail', 'requested_at', 'dispatched_at']


class OrderSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'menu', 'table', 'state', 'detail', 'requested_at', 'dispatched_at']
