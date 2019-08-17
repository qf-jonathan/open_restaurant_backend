from django.urls import path, include
from core.views import Index, Kitchen, AmbientViewset, MenuViewSet, TableViewSet, OrderViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('ambient', AmbientViewset, basename='ambient')
router.register('menu', MenuViewSet)
router.register('table', TableViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('test/kitchen/', Kitchen.as_view()),
    path('test/<str:ambient_name>/', Index.as_view()),
]
