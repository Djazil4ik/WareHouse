from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, ProductMaterialViewSet, MaterialViewSet, P_MViewSet

router = routers.DefaultRouter()

router.register('product', ProductViewSet)
router.register('product_material', P_MViewSet)
router.register('material', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-material/', ProductMaterialViewSet.as_view())
]