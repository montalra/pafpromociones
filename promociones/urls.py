from django.urls import path

from .views import EmpresaRegistro,EmpresaLista, EmpresaActualizar, EmpresaEliminar
from .views import SucursalRegistro,SucursalLista,SucursalActualizar, SucursalEliminar
from .views import TipoIdentificacionRegistro,TipoIdentificacionLista,TipoIdentificacionActualizar,TipoIdentificacionEliminar
from .views import VendedorRegistro,VendedorLista, VendedorActualizar, VendedorEliminar
from .views import GruposProveedorRegistro,GruposProveedorLista, GruposProveedorActualizar, GruposProveedorEliminar
from .views import UnidadesMedidaRegistro,UnidadesMedidaLista, UnidadesMedidaActualizar, UnidadesMedidaEliminar
from .views import LineasArticulosLista, LineasArticulosRegistro, LineasArticulosActualizar, LineasArticulosEliminar
from .views import SublineasArticulosLista, SublineasArticulosRegistro, SublineasArticulosActualizar, SublineasArticulosEliminar
from .views import MarcasRegistro, MarcasLista, MarcasActualizar, MarcasEliminar
from .views import ArticulosRegistro,ArticulosLista, ArticulosActualizar,ArticulosEliminar
from .views import ArticulosBonificadoRegistro,ArticulosBonificadoLista, ArticulosBonificadoActualizar,ArticulosBonificadoEliminar
from .views import CondicionVentaRegistro,CondicionVentaLista,CondicionVentaActualizar,CondicionVentaEliminar
from .views import TipoPedidoActualizar, TipoPedidoEliminar, TipoPedidoLista, TipoPedidoRegistro
from .views import CanalClienteRegistro, CanalClienteLista, CanalClienteActualizar, CanalClienteEliminar
from .views import ClienteRegistro, ClienteLista, ClienteActualizar, ClienteEliminar
from .views import NotaVentaActualizar, NotaVentaEliminar, NotaVentaLista, NotaVentaRegistro
from .views import ItemNotaVentaEliminar,ItemNotaVentaActualizar, ItemNotaVentaDetalle, ItemNotaVentaRegistro
from .views import TipoPromocionLista,TipoPromocionRegistro, TipoPromocionActualizar,TipoPromocionEliminar
from .views import PromocionDetalle, PromocionRegistro,PromocionActualizar,PromocionEliminar
from .views import UsuarioRegistro,  UsuarioLista,  UsuarioActualizar,  UsuarioEliminar
from .views import logout_user
from .import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path ('index/', views.index, name='index'),
    path('empresa/nueva/', EmpresaRegistro, name='nuevo_empresa'),
    path('empresa/listar/', EmpresaLista, name='empresa_lista'),
    path('empresa/editar/<str:empresa_id>/', EmpresaActualizar, name='empresa_actualizar'),
    path('empresa/eliminar/<str:empresa_id>/', EmpresaEliminar, name='empresa_eliminar'),

    path('sucursal/nueva/', SucursalRegistro, name='nuevo_sucursal'),
    path('sucursal/listar/', SucursalLista, name='sucursal_lista'),
    path('sucursal/<str:sucursal_id>/actualizar/', SucursalActualizar, name='sucursal_actualizar'),
    path('sucursal/<str:sucursal_id>/eliminar/', SucursalEliminar, name='sucursal_eliminar'),

    path('tipoidentificacion/nueva/', TipoIdentificacionRegistro, name='nuevo_tipoidentificacion'),
    path('tipoidentificacion/listar/', TipoIdentificacionLista, name='tipoidentificacion_lista'),
    path('tipoidentificacion/<str:tipo_identificacion_id>/actualizar/', TipoIdentificacionActualizar, name='tipoidentificacion_actualizar'),
    path('tipoidentificacion/<str:tipo_identificacion_id>/eliminar/', TipoIdentificacionEliminar, name='tipoidentificacion_eliminar'),

    path('vendedor/nueva/', VendedorRegistro, name='nuevo_vendedor'),
    path('vendedor/listar/', VendedorLista, name='vendedor_lista'),
    path('vendedor/<str:vendedor_id>/actualizar/', VendedorActualizar, name='vendedor_actualizar'),
    path('vendedor/<str:vendedor_id>/eliminar/', VendedorEliminar, name='vendedor_eliminar'),

    path('gruposproveedor/nueva/', GruposProveedorRegistro, name='nuevo_grupos_proveedor'),
    path('gruposproveedor/listar/', GruposProveedorLista, name='grupos_proveedor_lista'),
    path('gruposproveedor/<str:grupo_id>/actualizar/', GruposProveedorActualizar, name='grupos_proveedor_actualizar'),
    path('gruposproveedor/<str:grupo_id>/eliminar/', GruposProveedorEliminar, name='grupos_proveedor_eliminar'),


    path('unidadesmedida/nueva/', UnidadesMedidaRegistro, name='nuevo_unidades_medida'),
    path('unidadesmedida/listar/', UnidadesMedidaLista, name='unidades_medida_lista'),
    path('unidadesmedida/<str:unidad_medida_id>/actualizar/', UnidadesMedidaActualizar, name='unidades_medida_actualizar'),
    path('unidadesmedida/<str:unidad_medida_id>/eliminar/', UnidadesMedidaEliminar, name='unidades_medida_eliminar'),


    path('lineasArticulos/nueva/', LineasArticulosRegistro, name='nuevo_lineasArticulos'),
    path('lineasArticulos/listar/', LineasArticulosLista, name='lineasArticulos_lista'),
    path('lineasArticulos/editar/<str:linea_id>/', LineasArticulosActualizar, name='lineasArticulos_actualizar'),
    path('lineasArticulos/eliminar/<str:linea_id>/', LineasArticulosEliminar, name='lineasArticulos_eliminar'),

    path('sublineasArticulos/nueva/', SublineasArticulosRegistro, name='nuevo_sublineasArticulos'),
    path('sublineasArticulos/listar/', SublineasArticulosLista, name='sublineasArticulos_lista'),
    path('sublineasArticulos/editar/<str:sublinea_id>/', SublineasArticulosActualizar, name='sublineasArticulos_actualizar'),
    path('sublineasArticulos/eliminar/<str:sublinea_id>/', SublineasArticulosEliminar, name='sublineasArticulos_eliminar'),

    path('marcas/nueva/', MarcasRegistro, name='nuevo_marcas'),
    path('marcas/listar/', MarcasLista, name='marcas_lista'),
    path('marcas/<str:marca_id>/actualizar/', MarcasActualizar, name='marcas_actualizar'),
    path('marcas/<str:marca_id>/eliminar/', MarcasEliminar, name='marcas_eliminar'),

    path('articulos/nueva/', ArticulosRegistro, name='nuevo_articulos'),
    path('articulos/listar/', ArticulosLista, name='articulos_lista'),
    path('articulos/<str:articulo_id>/actualizar/', ArticulosActualizar, name='articulos_actualizar'),
    path('articulos/<str:articulo_id>/eliminar/', ArticulosEliminar, name='articulos_eliminar'),

    path('articulobonificado/nueva/', ArticulosBonificadoRegistro, name='nuevo_articulosbonificado'),
    path('articulobonificado/listar/', ArticulosBonificadoLista, name='articulosbonificado_lista'),
    path('articulobonificado/<str:articulo_bonificado_id>/actualizar/', ArticulosBonificadoActualizar, name='articulosbonificado_actualizar'),
    path('articulobonificado/<str:articulo_bonificado_id>/eliminar/', ArticulosBonificadoEliminar, name='articulosbonificado_eliminar'),

    path('cventa/nueva/', CondicionVentaRegistro, name='nuevo_cventa'),
    path('cventa/listar/', CondicionVentaLista, name='cventa_lista'),
    path('cventa/<str:condicion_venta>/actualizar/', CondicionVentaActualizar, name='cventa_actualizar'),
    path('cventa/<str:condicion_venta>/eliminar/', CondicionVentaEliminar, name='cventa_eliminar'),
  
    path('tipopedido/nueva/', TipoPedidoRegistro, name='nuevo_tipopedido'),
    path('tipopedido/listar/', TipoPedidoLista, name='tipopedido_lista'),
    path('tipopedido/<str:tipo_pedido_id>/actualizar/', TipoPedidoActualizar, name='tipopedido_actualizar'),
    path('tipopedido/<str:tipo_pedido_id>/eliminar/', TipoPedidoEliminar, name='tipopedido_eliminar'),
   
    path('canalcliente/nueva/', CanalClienteRegistro, name='nuevo_canalcliente'),
    path('canalcliente/listar/', CanalClienteLista, name='canalcliente_lista'),
    path('canalcliente/<str:canal_cliente_id>/actualizar', CanalClienteActualizar, name='canalcliente_actualizar'),
    path('canalcliente/<str:canal_cliente_id>/eliminar/', CanalClienteEliminar, name='canalcliente_eliminar'),

    path('cliente/nueva/', ClienteRegistro, name='nuevo_cliente'),
    path('cliente/listar/', ClienteLista, name='cliente_lista'),
    path('cliente/<str:cliente_id>/actualizar/', ClienteActualizar, name='cliente_actualizar'),
    path('cliente/<str:cliente_id>/eliminar/', ClienteEliminar, name='cliente_eliminar'),

    path('notaventa/nueva/', NotaVentaRegistro, name='nuevo_notaventa'),
    path('notaventa/listar/', NotaVentaLista, name='notaventa_lista'),
    path('notaventa/<str:nota_venta_id>/actualizar/', NotaVentaActualizar, name='notaventa_actualizar'),
    path('notaventa/<str:nota_venta_id>/eliminar/', NotaVentaEliminar, name='notaventa_eliminar'),

    path('itemnotaventa/nueva/', ItemNotaVentaRegistro, name='nuevo_itemnotaventa'),
    path('itemnotaventa/<str:item_id>/detalle/', ItemNotaVentaDetalle, name='itemnotaventa_detalle'),
    path('itemnotaventa/<str:item_id>/actualizar/', ItemNotaVentaActualizar, name='itemnotaventa_actualizar'),
    path('itemnotaventa/<str:item_id>/eliminar/', ItemNotaVentaEliminar, name='itemnotaventa_eliminar'),

    path('usuario/nueva/', UsuarioRegistro, name='nuevo_usuario'),
    path('usuario/listar/', UsuarioLista, name='usuario_lista'),
    path('usuario/editar/<str:id>/', UsuarioActualizar, name='usuario_actualizar'),
    path('eliminar/<str:id>/', UsuarioEliminar, name='usuario_eliminar'),

    path('tipopromocion/nueva/', TipoPromocionRegistro, name='nuevo_tipopromocion'),
    path('tipopromocion/listar/', TipoPromocionLista, name='tipopromocion_lista'),
    path('tipopromocion/<str:tipo_promocion_id>/actualizar/', TipoPromocionActualizar, name='tipopromocion_actualizar'),
    path('tipopromocion/<str:tipo_promocion_id>/eliminar/', TipoPromocionEliminar, name='tipopromocion_eliminar'),
    
    path('promocion/nueva/', PromocionRegistro, name='nuevo_promocion'),
    path('promocion/<str:promocion_id>/detalle/', PromocionDetalle, name='promocion_detalle'),
    path('promocion/<str:promocion_id>/actualizar/', PromocionActualizar, name='promocion_actualizar'),
    path('promocion/<str:promocion_id>/eliminar/', PromocionEliminar, name='promocion_eliminar'),

    path('logout/', logout_user, name='logout'),




]

