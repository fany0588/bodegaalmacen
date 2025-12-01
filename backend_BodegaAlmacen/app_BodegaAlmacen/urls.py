from django.urls import path
from .views import (
    index,  # Vista principal
    # Vistas CRUD de Productos
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    # Vistas CRUD de Categorías
    CategoriaListView,
    CategoriaDetailView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    # Vistas CRUD de Proveedores
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
    # Vistas CRUD de Empleados
    EmpleadoListView,
    EmpleadoDetailView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDeleteView,
    # Vistas CRUD de Entradas de Producto
    EntradaListView,
    EntradaDetailView,
    EntradaCreateView,
    EntradaUpdateView,
    EntradaDeleteView,
    # Vistas CRUD de Salidas de Producto
    SalidaListView,
    SalidaDetailView,
    SalidaCreateView,
    SalidaUpdateView,
    SalidaDeleteView,
    # Vistas CRUD de Inventario Físico
    InventarioFisicoListView,
    InventarioFisicoDetailView,
    InventarioFisicoCreateView,
    InventarioFisicoUpdateView,
    InventarioFisicoDeleteView,
    # API ViewSets
    CategoriaAlmacenViewSet,
    ProveedorAlmacenViewSet,
    EmpleadoAlmacenViewSet,
    ProductoAlmacenViewSet,
    EntradaProductoViewSet,
    SalidaProductoViewSet,
    InventarioFisicoViewSet
)

urlpatterns = [
    # --- Rutas de la Interfaz Web ---
    path('', index, name='index'),
    
    # CRUD de Productos
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_edit'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # CRUD de Categorías
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    # CRUD de Proveedores
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_edit'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'),

    # CRUD de Empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    
    # CRUD de Entradas de Producto
    path('entradas/', EntradaListView.as_view(), name='entrada_list'),
    path('entradas/nueva/', EntradaCreateView.as_view(), name='entrada_create'),
    path('entradas/<int:pk>/', EntradaDetailView.as_view(), name='entrada_detail'),
    path('entradas/<int:pk>/editar/', EntradaUpdateView.as_view(), name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/', EntradaDeleteView.as_view(), name='entrada_delete'),
    
    # CRUD de Salidas de Producto
    path('salidas/', SalidaListView.as_view(), name='salida_list'),
    path('salidas/nueva/', SalidaCreateView.as_view(), name='salida_create'),
    path('salidas/<int:pk>/', SalidaDetailView.as_view(), name='salida_detail'),
    path('salidas/<int:pk>/editar/', SalidaUpdateView.as_view(), name='salida_edit'),
    path('salidas/<int:pk>/eliminar/', SalidaDeleteView.as_view(), name='salida_delete'),

    # CRUD de Inventario Físico
    path('inventarios/', InventarioFisicoListView.as_view(), name='inventario_list'),
    path('inventarios/nuevo/', InventarioFisicoCreateView.as_view(), name='inventario_create'),
    path('inventarios/<int:pk>/', InventarioFisicoDetailView.as_view(), name='inventario_detail'),
    path('inventarios/<int:pk>/editar/', InventarioFisicoUpdateView.as_view(), name='inventario_edit'),
    path('inventarios/<int:pk>/eliminar/', InventarioFisicoDeleteView.as_view(), name='inventario_delete'),

    # --- Rutas de la API (prefijadas con api/) ---
    
    # Categorias API
    path('api/categorias/', CategoriaAlmacenViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_categoria_list'),
    path('api/categorias/<int:pk>/', CategoriaAlmacenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_categoria_detail'),

    # Proveedores API
    path('api/proveedores/', ProveedorAlmacenViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_proveedor_list'),
    path('api/proveedores/<int:pk>/', ProveedorAlmacenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_proveedor_detail'),

    # Empleados API
    path('api/empleados/', EmpleadoAlmacenViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_empleado_list'),
    path('api/empleados/<int:pk>/', EmpleadoAlmacenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_empleado_detail'),
    
    # Entradas API
    path('api/entradas/', EntradaProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_entrada_list'),
    path('api/entradas/<int:pk>/', EntradaProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_entrada_detail'),

    # Productos API
    path('api/productos/', ProductoAlmacenViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_producto_list'),
    path('api/productos/<int:pk>/', ProductoAlmacenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_producto_detail'),

    # Salidas API
    path('api/salidas/', SalidaProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_salida_list'),
    path('api/salidas/<int:pk>/', SalidaProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_salida_detail'),

    # Inventarios API
    path('api/inventarios/', InventarioFisicoViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_inventario_list'),
    path('api/inventarios/<int:pk>/', InventarioFisicoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='api_inventario_detail'),
]
