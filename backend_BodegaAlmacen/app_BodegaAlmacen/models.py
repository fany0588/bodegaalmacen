
from django.db import models

class CategoriaAlmacen(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField(null=True, blank=True)
    temperatura_ideal = models.CharField(max_length=50, null=True, blank=True)
    tipo_almacenamiento = models.CharField(max_length=50, null=True, blank=True)
    es_peligroso = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_categoria


class ProveedorAlmacen(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    contacto_persona = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    direccion_proveedor = models.CharField(max_length=255, null=True, blank=True)
    ruc = models.CharField(max_length=20, null=True, blank=True)
    pais_origen = models.CharField(max_length=50, null=True, blank=True)
    condiciones_pago = models.CharField(max_length=100, null=True, blank=True)
    tiempo_entrega_dias = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_proveedor


class EmpleadoAlmacen(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    turno = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    licencia_manejo_montacargas = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ProductoAlmacen(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    codigo_sku = models.CharField(max_length=50, unique=True)
    stock_actual = models.IntegerField(default=0)
    ubicacion_almacen = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(CategoriaAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    volumen_m3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_ultimo_movimiento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre_producto


class EntradaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_entrada = models.IntegerField(default=0)
    fecha_entrada = models.DateTimeField(null=True, blank=True)
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    num_factura_compra = models.CharField(max_length=50, null=True, blank=True)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    empleado_recepcion = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Entrada {self.id} - {self.producto.nombre_producto}"


class SalidaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_salida = models.IntegerField(default=0)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    destino = models.CharField(max_length=100, null=True, blank=True)
    id_cliente_salida = models.IntegerField(null=True, blank=True)
    num_pedido_salida = models.CharField(max_length=50, null=True, blank=True)
    empleado_despacho = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    motivo_salida = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Salida {self.id} - {self.producto.nombre_producto}"


class InventarioFisico(models.Model):
    fecha_inventario = models.DateField(null=True, blank=True)
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    stock_sistema = models.IntegerField(default=0)
    stock_fisico = models.IntegerField(default=0)
    diferencia = models.IntegerField(default=0) # This can be calculated
    empleado_realizo = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Inventario {self.id} - {self.producto.nombre_producto}"
