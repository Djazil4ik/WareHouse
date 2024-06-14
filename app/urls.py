from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, ProductMaterialViewSet, MaterialViewSet

router = routers.DefaultRouter()

router.register('product', ProductViewSet)
# router.register('p-m', PMViewSet)
router.register('material', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-material/', ProductMaterialViewSet.as_view())
]