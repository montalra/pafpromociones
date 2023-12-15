from django.contrib import admin
from .models import Empresa,Sucursal,TipoIdentificacion, Vendedor,GruposProveedor, UnidadesMedida, LineasArticulos,SublineasArticulos,Marcas, Articulos,  ArticulosBonificado, CondicionesVenta, TipoPedido,CanalCliente,Cliente,NotaVenta, ItemNotaVenta, Promocion, TipoPromocion, Usuario

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(TipoIdentificacion)
admin.site.register(Vendedor)
admin.site.register(GruposProveedor)
admin.site.register(UnidadesMedida)
admin.site.register(LineasArticulos)
admin.site.register(SublineasArticulos)
admin.site.register(Marcas)
admin.site.register(Articulos)
admin.site.register(ArticulosBonificado)
admin.site.register(CondicionesVenta)
admin.site.register(TipoPedido)
admin.site.register(CanalCliente)
admin.site.register(Cliente)
admin.site.register(TipoPromocion)
admin.site.register(Promocion)
admin.site.register(NotaVenta)
admin.site.register(ItemNotaVenta)
admin.site.register(Usuario)

