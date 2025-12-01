from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import (
    CategoriaAlmacen, ProveedorAlmacen, EmpleadoAlmacen, ProductoAlmacen, EntradaProducto, SalidaProducto, InventarioFisico
)
from .serializers import (
    CategoriaAlmacenSerializer, ProveedorAlmacenSerializer, EmpleadoAlmacenSerializer, ProductoAlmacenSerializer, EntradaProductoSerializer, SalidaProductoSerializer, InventarioFisicoSerializer
)

# Vista para la página de inicio
def index(request):
    return render(request, 'index.html')

# Vistas CRUD de ProductoAlmacen
class ProductoListView(ListView):
    model = ProductoAlmacen
    template_name = 'ProductoAlmacen/ProductoList.html'
    context_object_name = 'object_list'

class ProductoDetailView(DetailView):
    model = ProductoAlmacen
    template_name = 'ProductoAlmacen/ProductoDetail.html'

class ProductoCreateView(CreateView):
    model = ProductoAlmacen
    template_name = 'ProductoAlmacen/ProductoForm.html'
    fields = ['nombre_producto', 'codigo_sku', 'descripcion', 'stock_actual', 'categoria', 'proveedor', 'ubicacion_almacen', 'peso_kg', 'volumen_m3']
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = ProductoAlmacen
    template_name = 'ProductoAlmacen/ProductoForm.html'
    fields = ['nombre_producto', 'codigo_sku', 'descripcion', 'stock_actual', 'categoria', 'proveedor', 'ubicacion_almacen', 'peso_kg', 'volumen_m3']
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = ProductoAlmacen
    template_name = 'ProductoAlmacen/ProductoConfirm_delete.html'
    success_url = reverse_lazy('producto_list')

# Vistas CRUD de CategoriaAlmacen
class CategoriaListView(ListView):
    model = CategoriaAlmacen
    template_name = 'CategoriaAlmacen/CategoriaList.html'
    context_object_name = 'object_list'

class CategoriaDetailView(DetailView):
    model = CategoriaAlmacen
    template_name = 'CategoriaAlmacen/CategoriaDetail.html'

class CategoriaCreateView(CreateView):
    model = CategoriaAlmacen
    template_name = 'CategoriaAlmacen/CategoriaForm.html'
    fields = ['nombre_categoria', 'descripcion_categoria', 'temperatura_ideal', 'tipo_almacenamiento', 'es_peligroso']
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = CategoriaAlmacen
    template_name = 'CategoriaAlmacen/CategoriaForm.html'
    fields = ['nombre_categoria', 'descripcion_categoria', 'temperatura_ideal', 'tipo_almacenamiento', 'es_peligroso']
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = CategoriaAlmacen
    template_name = 'CategoriaAlmacen/CategoriaConfirm_delete.html'
    success_url = reverse_lazy('categoria_list')

# Vistas CRUD de ProveedorAlmacen
class ProveedorListView(ListView):
    model = ProveedorAlmacen
    template_name = 'ProveedorAlmacen/ProveedorList.html'
    context_object_name = 'object_list'

class ProveedorDetailView(DetailView):
    model = ProveedorAlmacen
    template_name = 'ProveedorAlmacen/ProveedorDetail.html'

class ProveedorCreateView(CreateView):
    model = ProveedorAlmacen
    template_name = 'ProveedorAlmacen/ProveedorForm.html'
    fields = ['nombre_proveedor', 'contacto_persona', 'telefono', 'email', 'direccion_proveedor', 'ruc', 'pais_origen', 'condiciones_pago', 'tiempo_entrega_dias']
    success_url = reverse_lazy('proveedor_list')

class ProveedorUpdateView(UpdateView):
    model = ProveedorAlmacen
    template_name = 'ProveedorAlmacen/ProveedorForm.html'
    fields = ['nombre_proveedor', 'contacto_persona', 'telefono', 'email', 'direccion_proveedor', 'ruc', 'pais_origen', 'condiciones_pago', 'tiempo_entrega_dias']
    success_url = reverse_lazy('proveedor_list')

class ProveedorDeleteView(DeleteView):
    model = ProveedorAlmacen
    template_name = 'ProveedorAlmacen/ProveedorConfirm_delete.html'
    success_url = reverse_lazy('proveedor_list')

# Vistas CRUD de EmpleadoAlmacen
class EmpleadoListView(ListView):
    model = EmpleadoAlmacen
    template_name = 'EmpleadoAlmacen/EmpleadoList.html'
    context_object_name = 'object_list'

class EmpleadoDetailView(DetailView):
    model = EmpleadoAlmacen
    template_name = 'EmpleadoAlmacen/EmpleadoDetail.html'

class EmpleadoCreateView(CreateView):
    model = EmpleadoAlmacen
    template_name = 'EmpleadoAlmacen/EmpleadoForm.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_contratacion', 'cargo', 'turno', 'telefono', 'email', 'licencia_manejo_montacargas']
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = EmpleadoAlmacen
    template_name = 'EmpleadoAlmacen/EmpleadoForm.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_contratacion', 'cargo', 'turno', 'telefono', 'email', 'licencia_manejo_montacargas']
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = EmpleadoAlmacen
    template_name = 'EmpleadoAlmacen/EmpleadoConfirm_delete.html'
    success_url = reverse_lazy('empleado_list')

# Vistas CRUD de EntradaProducto
class EntradaListView(ListView):
    model = EntradaProducto
    template_name = 'EntradaProducto/EntradaList.html'
    context_object_name = 'object_list'
    ordering = ['-fecha_entrada']

class EntradaDetailView(DetailView):
    model = EntradaProducto
    template_name = 'EntradaProducto/EntradaDetail.html'

class EntradaCreateView(CreateView):
    model = EntradaProducto
    template_name = 'EntradaProducto/EntradaForm.html'
    fields = ['producto', 'cantidad_entrada', 'fecha_entrada', 'proveedor', 'num_factura_compra', 'costo_unitario', 'empleado_recepcion', 'observaciones']
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        with transaction.atomic():
            self.object = form.save()
            producto = self.object.producto
            producto.stock_actual += self.object.cantidad_entrada
            producto.save()
        return HttpResponseRedirect(self.get_success_url())

class EntradaUpdateView(UpdateView):
    model = EntradaProducto
    template_name = 'EntradaProducto/EntradaForm.html'
    fields = ['producto', 'cantidad_entrada', 'fecha_entrada', 'proveedor', 'num_factura_compra', 'costo_unitario', 'empleado_recepcion', 'observaciones']
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        with transaction.atomic():
            entrada_original = get_object_or_404(EntradaProducto, pk=self.object.pk)
            producto_original = entrada_original.producto
            cantidad_original = entrada_original.cantidad_entrada

            nueva_entrada = form.save(commit=False)
            producto_nuevo = nueva_entrada.producto
            cantidad_nueva = nueva_entrada.cantidad_entrada

            if producto_original.pk == producto_nuevo.pk:
                diferencia = cantidad_nueva - cantidad_original
                producto_nuevo.stock_actual += diferencia
                producto_nuevo.save()
            else:
                producto_original.stock_actual -= cantidad_original
                producto_original.save()
                producto_nuevo.stock_actual += cantidad_nueva
                producto_nuevo.save()
            
            nueva_entrada.save()
            form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

class EntradaDeleteView(DeleteView):
    model = EntradaProducto
    template_name = 'EntradaProducto/EntradaConfirm_delete.html'
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        with transaction.atomic():
            entrada = self.get_object()
            producto = entrada.producto
            if producto.stock_actual >= entrada.cantidad_entrada:
                producto.stock_actual -= entrada.cantidad_entrada
                producto.save()
            else:
                form.add_error(None, f"No se puede borrar la entrada. El stock actual ({producto.stock_actual}) es menor a la cantidad de la entrada ({entrada.cantidad_entrada}).")
                return self.form_invalid(form)
        return super().form_valid(form)

# Vistas CRUD de SalidaProducto
class SalidaListView(ListView):
    model = SalidaProducto
    template_name = 'SalidaProducto/SalidaList.html'
    context_object_name = 'object_list'
    ordering = ['-fecha_salida']

class SalidaDetailView(DetailView):
    model = SalidaProducto
    template_name = 'SalidaProducto/SalidaDetail.html'

class SalidaCreateView(CreateView):
    model = SalidaProducto
    template_name = 'SalidaProducto/SalidaForm.html'
    fields = ['producto', 'cantidad_salida', 'fecha_salida', 'destino', 'id_cliente_salida', 'num_pedido_salida', 'empleado_despacho', 'motivo_salida']
    success_url = reverse_lazy('salida_list')

    def form_valid(self, form):
        with transaction.atomic():
            salida = form.save(commit=False)
            producto = salida.producto
            if producto.stock_actual < salida.cantidad_salida:
                form.add_error('cantidad_salida', f"No hay stock suficiente. Stock actual: {producto.stock_actual}")
                return self.form_invalid(form)
            
            producto.stock_actual -= salida.cantidad_salida
            producto.save()
            salida.save()
            self.object = salida
        return HttpResponseRedirect(self.get_success_url())

class SalidaUpdateView(UpdateView):
    model = SalidaProducto
    template_name = 'SalidaProducto/SalidaForm.html'
    fields = ['producto', 'cantidad_salida', 'fecha_salida', 'destino', 'id_cliente_salida', 'num_pedido_salida', 'empleado_despacho', 'motivo_salida']
    success_url = reverse_lazy('salida_list')

    def form_valid(self, form):
        with transaction.atomic():
            salida_original = get_object_or_404(SalidaProducto, pk=self.object.pk)
            producto_original = salida_original.producto
            cantidad_original = salida_original.cantidad_salida

            nueva_salida = form.save(commit=False)
            producto_nuevo = nueva_salida.producto
            cantidad_nueva = nueva_salida.cantidad_salida

            if producto_original.pk == producto_nuevo.pk:
                diferencia = cantidad_original - cantidad_nueva
                if producto_nuevo.stock_actual < -diferencia:
                    form.add_error('cantidad_salida', f"No hay stock suficiente. Stock actual: {producto_nuevo.stock_actual}")
                    return self.form_invalid(form)
                producto_nuevo.stock_actual += diferencia
                producto_nuevo.save()
            else:
                producto_original.stock_actual += cantidad_original
                producto_original.save()

                if producto_nuevo.stock_actual < cantidad_nueva:
                    form.add_error('cantidad_salida', f"No hay stock suficiente para el nuevo producto. Stock disponible: {producto_nuevo.stock_actual}")
                    producto_original.stock_actual -= cantidad_original
                    producto_original.save()
                    return self.form_invalid(form)
                
                producto_nuevo.stock_actual -= cantidad_nueva
                producto_nuevo.save()
            
            nueva_salida.save()
            form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

class SalidaDeleteView(DeleteView):
    model = SalidaProducto
    template_name = 'SalidaProducto/SalidaConfirm_delete.html'
    success_url = reverse_lazy('salida_list')

    def form_valid(self, form):
        with transaction.atomic():
            salida = self.get_object()
            producto = salida.producto
            producto.stock_actual += salida.cantidad_salida
            producto.save()
        return super().form_valid(form)

# Vistas CRUD de InventarioFisico
class InventarioFisicoListView(ListView):
    model = InventarioFisico
    template_name = 'InventarioFisicoAlmacen/InventarioFisicoList.html'
    context_object_name = 'object_list'
    ordering = ['-fecha_inventario']

class InventarioFisicoDetailView(DetailView):
    model = InventarioFisico
    template_name = 'InventarioFisicoAlmacen/InventarioFisicoDetail.html'

class InventarioFisicoCreateView(CreateView):
    model = InventarioFisico
    template_name = 'InventarioFisicoAlmacen/InventarioFisicoForm.html'
    fields = ['producto', 'stock_fisico', 'empleado_realizo', 'comentarios', 'fecha_inventario']
    success_url = reverse_lazy('inventario_list')

    def form_valid(self, form):
        with transaction.atomic():
            inventario = form.save(commit=False)
            producto = inventario.producto
            
            inventario.stock_sistema = producto.stock_actual
            inventario.diferencia = inventario.stock_fisico - inventario.stock_sistema
            inventario.ultima_actualizacion = timezone.now()
            
            inventario.save()
            self.object = inventario
        return HttpResponseRedirect(self.get_success_url())

class InventarioFisicoUpdateView(UpdateView):
    model = InventarioFisico
    template_name = 'InventarioFisicoAlmacen/InventarioFisicoForm.html'
    fields = ['producto', 'stock_fisico', 'empleado_realizo', 'comentarios', 'fecha_inventario']
    success_url = reverse_lazy('inventario_list')

    def form_valid(self, form):
        with transaction.atomic():
            inventario = form.save(commit=False)
            producto = inventario.producto
            
            inventario.stock_sistema = producto.stock_actual
            inventario.diferencia = inventario.stock_fisico - inventario.stock_sistema
            inventario.ultima_actualizacion = timezone.now()
            
            inventario.save()
        return HttpResponseRedirect(self.get_success_url())

class InventarioFisicoDeleteView(DeleteView):
    model = InventarioFisico
    template_name = 'InventarioFisicoAlmacen/InventarioFisicoConfirm_delete.html'
    success_url = reverse_lazy('inventario_list')


# --- API ViewSets ---
class CategoriaAlmacenViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAlmacen.objects.all()
    serializer_class = CategoriaAlmacenSerializer

class ProveedorAlmacenViewSet(viewsets.ModelViewSet):
    queryset = ProveedorAlmacen.objects.all()
    serializer_class = ProveedorAlmacenSerializer

class EmpleadoAlmacenViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoAlmacen.objects.all()
    serializer_class = EmpleadoAlmacenSerializer

class ProductoAlmacenViewSet(viewsets.ModelViewSet):
    queryset = ProductoAlmacen.objects.all()
    serializer_class = ProductoAlmacenSerializer

class EntradaProductoViewSet(viewsets.ModelViewSet):
    queryset = EntradaProducto.objects.all()
    serializer_class = EntradaProductoSerializer

class SalidaProductoViewSet(viewsets.ModelViewSet):
    queryset = SalidaProducto.objects.all()
    serializer_class = SalidaProductoSerializer

class InventarioFisicoViewSet(viewsets.ModelViewSet):
    queryset = InventarioFisico.objects.all()
    serializer_class = InventarioFisicoSerializer
