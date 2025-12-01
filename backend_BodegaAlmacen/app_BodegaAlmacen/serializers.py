from rest_framework import serializers
from .models import (
    CategoriaAlmacen, ProveedorAlmacen, EmpleadoAlmacen, ProductoAlmacen, EntradaProducto, SalidaProducto, InventarioFisico
)

class CategoriaAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAlmacen
        fields = '__all__'

class ProveedorAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorAlmacen
        fields = '__all__'

class EmpleadoAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoAlmacen
        fields = '__all__'

class ProductoAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAlmacen
        fields = '__all__'

class EntradaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaProducto
        fields = '__all__'

class SalidaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalidaProducto
        fields = '__all__'

class InventarioFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioFisico
        fields = '__all__'
