from rest_framework import viewsets, status
from .serializers import ProductSerializer, ProductMaterialSerializer, MaterialSerializer, ProductQuantitySerializer
from rest_framework.views import APIView, Response
from .models import Product, ProductMaterial, Material, Warehouse
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMaterialViewSet(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ProductMaterial.objects.all()
        serializer = ProductMaterialSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductQuantitySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            products_to_produce = serializer.validated_data

            result = []
            for product_info in products_to_produce:
                product_name = product_info['name']
                product_qty = product_info['quantity']
                product = get_object_or_404(Product, name=product_name)
                product_materials = ProductMaterial.objects.filter(product=product)

                materials_needed = []
                for pm in product_materials:
                    material_needed_qty = pm.quantity * product_qty
                    warehouses = Warehouse.objects.filter(material=pm.material)
                    for warehouse in warehouses:
                        if material_needed_qty <= 0:
                            break
                        if warehouse.remainder >= material_needed_qty:
                            materials_needed.append({
                                'warehouse_id': warehouse.id,
                                'material_name': pm.material.name,
                                'qty': material_needed_qty,
                                'price': warehouse.price
                            })
                            material_needed_qty = 0
                        else:
                            materials_needed.append({
                                'warehouse_id': warehouse.id,
                                'material_name': pm.material.name,
                                'qty': warehouse.remainder,
                                'price': warehouse.price
                            })
                            material_needed_qty -= warehouse.remainder

                    if material_needed_qty > 0:
                        materials_needed.append({
                            'warehouse_id': None,
                            'material_name': pm.material.name,
                            'qty': material_needed_qty,
                            'price': None
                        })

                result.append({
                    'product_name': product_name,
                    'product_qty': product_qty,
                    'product_materials': materials_needed
                })

            return Response({'result': result})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
