from decimal import Decimal
CANAL_MAYORISTA = '1'
CANAL_COBERTURA = '2'

def aplicar_promocion(item_nota_venta):
    promocion = item_nota_venta.promocion_aplicada

    if promocion:
        canal_cliente_id = item_nota_venta.nota_venta.cliente.canal_cliente.canal_cliente_id

        if canal_cliente_id == CANAL_MAYORISTA:
            # Cliente es MAYORISTA
            aplicar_promocion_mayorista(item_nota_venta, promocion)
        elif canal_cliente_id == CANAL_COBERTURA:
            # Cliente es de COBERTURA
            aplicar_promocion_cobertura(item_nota_venta, promocion)


def aplicar_promocion_mayorista(item_nota_venta, promocion):
    if item_nota_venta.articulo in promocion.articulo.all():
        if promocion.tipo_promocion == 'unidad':
            aplicar_promocion_unidad(item_nota_venta, promocion)
        elif promocion.tipo_promocion == 'soles':
            aplicar_promocion_soles(item_nota_venta, promocion)


def aplicar_promocion_unidad(item_nota_venta, promocion):
    if item_nota_venta.cantidad >= promocion.limite and item_nota_venta.cantidad == 48:
        item_nota_venta.bonificacion_unidades = 2
    elif item_nota_venta.cantidad >= 60:
        item_nota_venta.bonificacion_unidades = 2
    elif item_nota_venta.cantidad >= promocion.limite and item_nota_venta.cantidad == 72:
        item_nota_venta.bonificacion_unidades = 6
    else:
        item_nota_venta.bonificacion_unidades = 0

    item_nota_venta.precio_unitario = item_nota_venta.articulo.precio
    item_nota_venta.total_item_bruto = item_nota_venta.cantidad * item_nota_venta.precio_unitario
    item_nota_venta.cantidad_con_bonificacion = item_nota_venta.cantidad + item_nota_venta.bonificacion_unidades

    item_nota_venta.factor_descuento = (promocion.descuento / Decimal(100))
    item_nota_venta.descuento_unitario = item_nota_venta.factor_descuento * item_nota_venta.precio_unitario
    item_nota_venta.total_item = item_nota_venta.total_item_bruto - item_nota_venta.descuento_unitario
    item_nota_venta.es_bonificacion = True


def aplicar_promocion_soles(item_nota_venta, promocion):
    item_nota_venta.precio_unitario = item_nota_venta.articulo.precio
    item_nota_venta.total_item_bruto = item_nota_venta.precio_unitario * item_nota_venta.cantidad
    if (item_nota_venta.articulo.linea.linea_descripcion == 'Detergente' and
            item_nota_venta.total_item_bruto >= promocion.limite):
        item_nota_venta.factor_descuento = (promocion.descuento / Decimal(100))
        item_nota_venta.descuento_unitario = item_nota_venta.total_item_bruto * item_nota_venta.factor_descuento
        item_nota_venta.total_item = item_nota_venta.total_item_bruto - item_nota_venta.descuento_unitario
        item_nota_venta.es_bonificacion = True


def aplicar_promocion_cobertura(item_nota_venta, promocion):
    if item_nota_venta.articulo in promocion.articulo.all():
        if promocion.tipo_promocion == 'unidad':
            aplicar_promocion_unidad_caso3(item_nota_venta, promocion)



def aplicar_promocion_unidad_caso3(item_nota_venta, promocion):
    if item_nota_venta.cantidad > promocion.limite == 7:
        item_nota_venta.precio_unitario = item_nota_venta.articulo.precio
        item_nota_venta.total_item_bruto = item_nota_venta.cantidad * item_nota_venta.precio_unitario

        item_nota_venta.factor_descuento = (promocion.descuento / Decimal(100))
        item_nota_venta.descuento_unitario = item_nota_venta.total_item_bruto * item_nota_venta.factor_descuento
        item_nota_venta.total_item = item_nota_venta.total_item_bruto - item_nota_venta.descuento_unitario
        item_nota_venta.es_bonificacion = True
