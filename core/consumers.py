from channels.generic.websocket import AsyncJsonWebsocketConsumer
from core.models import Ambient, Order
from core.serializers import OrderSerializer, OrderSingleSerializer, AmbientDetailSerializer
from django.forms.models import model_to_dict

NEW_ORDER = 'new_order'
CHANGE_ORDER = 'change_order'
ATTENDANCE_GROUP_NAME = 'attention'


class AttendanceConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.attendance_group_name = ATTENDANCE_GROUP_NAME
        super().__init__(*args, **kwargs)

    async def connect(self):
        connection_type = self.scope['path'].strip('/').split('/')[-1]
        await self.channel_layer.group_add(
            self.attendance_group_name,
            self.channel_name
        )
        await self.accept()
        if connection_type == 'ambient':
            await self.send_ambients()
        if connection_type == 'kitchen':
            await self.send_orders()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.attendance_group_name,
            self.channel_name
        )

    async def receive_json(self, content):
        if content['type'] == NEW_ORDER:
            await self.process_new_order(content['data'])
        if content['type'] == CHANGE_ORDER:
            await self.process_order_state(content['data'])

    async def process_new_order(self, content):
        serializer = OrderSingleSerializer(data=content)
        if serializer.is_valid():
            created = model_to_dict(serializer.save())
            await self.channel_layer.group_send(
                self.attendance_group_name, {
                    'type': NEW_ORDER,
                    'created': created
                }
            )

    async def process_order_state(self, content):
        try:
            order = Order.objects.select_related('table__ambient').get(id=content['id'])
        except Order.DoesNotExist:
            order = None
        if order is not None:
            order.state = content['state']
            order.save()
            await self.channel_layer.group_send(
                self.attendance_group_name,
                {
                    'type': CHANGE_ORDER,
                    'changed': model_to_dict(order)
                }
            )

    async def send_ambients(self):
        ambients = Ambient.objects.prefetch_related('tables', 'tables__orders')
        serializer = AmbientDetailSerializer(ambients, many=True)
        await self.send_json({
            'type': 'initial_ambients',
            'ambients': serializer.data
        })

    async def send_orders(self):
        orders = Order.objects.select_related('menu', 'table')
        serializer = OrderSerializer(orders, many=True)
        await self.send_json({
            'type': 'initial_orders',
            'orders': serializer.data
        })

    async def new_order(self, event):
        await self.send_json({
            'type': NEW_ORDER,
            'order': event['created']
        })

    async def change_order(self, event):
        await self.send_json({
            'type': CHANGE_ORDER,
            'order': event['changed']
        })
