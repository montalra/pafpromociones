from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Empresa(models.Model):
    empresa_id = models.CharField (max_length=2, primary_key=True,unique=True )
    nro_documento = models.CharField(max_length=11, null=False, unique =True )
    razon_social = models.CharField(max_length=150, null= False)
    direccion = models.CharField(max_length=150, null= False)

    class Meta:
        db_table = 'empresa'

    def __str__(self) -> str:
        return '%s - %s '% (self.empresa_id, self.razon_social)

class Sucursal(models.Model):
    sucursal_id = models.CharField(max_length=4, primary_key=True,unique=True)
    empresa= models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)
    nombre_comercial = models.CharField(max_length=150,  null= False)
    direccion = models.CharField(max_length=150,null= False )

    class Meta:
        db_table = 'sucursal'

    def __str__(self)-> str:
        return '%s - %s ' % (self.sucursal_id, self.nombre_comercial)


class TipoIdentificacion(models.Model):
    tipo_identificacion_id = models.CharField(max_length=2, primary_key=True,unique=True)
    tipo_identificacion_nombre = models.CharField(max_length=100, null= False)

    class Meta:
        db_table = 'tipoidentificacion'

    def __str__(self)-> str:
        return '%s - %s ' % (self.tipo_identificacion_id, self.tipo_identificacion_nombre)

class Vendedor(models.Model):
    vendedor_id = models.AutoField(primary_key=True, unique=True)
    vendedor_codigo = models.CharField(max_length=15, unique=True, null= False)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.RESTRICT, null= False)
    nro_documento = models.CharField(max_length=11, null= False)
    nombres = models.CharField(max_length=150, null= False)
    direccion = models.CharField(max_length=150, null= False)
    correo_electronico = models.EmailField(max_length=255, null= False)
    nro_movil = models.CharField(max_length=15, null= False)
    empresa= models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)

    class Meta:
        db_table = 'vendedor'
        ordering =["vendedor_id"]

    def __str__(self)-> str:
        return '%s - %s - %s - %s' % (self.vendedor_id, self.vendedor_codigo, self.nro_documento,self.nombres)

    
class GruposProveedor(models.Model):
    grupo_id = models.AutoField(primary_key=True, unique=True)
    codigo_grupo = models.CharField(max_length=15, null= False)
    grupo_descripcion = models.CharField(max_length=100, null= False)
    empresa= models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)
    activo = models.BooleanField(default=True)
    responsable_grupo = models.ForeignKey(Vendedor, on_delete=models.RESTRICT, null= False)

    class Meta:
        db_table = 'grupos_proveedor'
        ordering =["grupo_id"]

    def __str__(self)-> str:
        return '%s - %s  - %s - %s ' % (self.grupo_id, self.codigo_grupo, self.grupo_descripcion,self.activo)


class UnidadesMedida(models.Model):
    unidad_medida_id = models.AutoField(primary_key=True,unique=True)
    unidad_nombre = models.CharField(max_length=150, unique=True, null= False)

    class Meta:
        db_table = 'unidades_medida'
        ordering =["unidad_medida_id"]

    def __str__(self)-> str:
        return '%s - %s ' % (self.unidad_medida_id, self.unidad_nombre)

class LineasArticulos(models.Model):
    linea_id = models.AutoField(primary_key=True, unique=True)
    codigo_linea = models.CharField(max_length=15, null= False)
    linea_descripcion = models.CharField(max_length=100, null= False)
    grupo= models.ForeignKey(GruposProveedor, on_delete=models.RESTRICT, null= False)
    activo = models.BooleanField(default=True)
    responsable_linea = models.ForeignKey(Vendedor, on_delete=models.RESTRICT, null= False)
    class Meta:
        db_table = 'lineas_articulos'
        ordering =["linea_id"]

    def __str__(self)-> str:
        return '%s - %s - %s' % (self.linea_id, self.codigo_linea,self.linea_descripcion )


class SublineasArticulos(models.Model):
    sublinea_id = models.AutoField(primary_key=True, unique=True)
    codigo_sublinea = models.CharField(max_length=15, null= False)
    sublinea_descripcion = models.CharField(max_length=100, null= False)
    linea= models.ForeignKey(LineasArticulos, on_delete=models.RESTRICT, null= False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sublineas_articulos'
        ordering =["sublinea_id"]  

    def __str__(self)-> str:
        return '%s - %s - %s- %s' % (self.sublinea_id, self.codigo_sublinea, self.sublinea_descripcion,self.estado)


class Marcas(models.Model):
    marca_id = models.AutoField(primary_key=True, unique=True)
    codigo_marca = models.CharField(max_length=14,unique=True, null= False)
    marca_nombre = models.CharField(max_length=150,unique=True, null= False)

    class Meta:
        db_table = 'marcas'
        ordering =["marca_id"]

    def __str__(self)-> str:
        return '%s - %s - %s' % (self.marca_id, self.codigo_marca, self.marca_nombre)

    
    
class Articulos(models.Model):
    articulo_id = models.AutoField(primary_key=True, unique=True)
    codigo_sku = models.CharField(max_length=25, null= False)
    nombre_articulo = models.CharField(max_length=50, null= False)
    unidad_medida= models.ForeignKey(UnidadesMedida, on_delete=models.RESTRICT, null= False )
    grupo = models.ForeignKey(GruposProveedor, on_delete=models.RESTRICT, null= False )
    linea = models.ForeignKey(LineasArticulos, on_delete=models.RESTRICT, null= False)
    sublinea= models.ForeignKey(SublineasArticulos, on_delete=models.RESTRICT, null= False)
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)
    factor_compra = models.PositiveIntegerField()
    factor_reparto = models.PositiveIntegerField()
    marca= models.ForeignKey(Marcas, on_delete=models.RESTRICT, null= False)

    class Meta:
        db_table = 'articulos'
        ordering =["articulo_id"]

    def __str__(self)-> str:
        return '%s - %s - %s' % (self.articulo_id, self.codigo_sku, self.nombre_articulo)
    
class ArticulosBonificado(models.Model):
    articulo_bonificado_id = models.AutoField(primary_key=True, unique=True)
    codigo_sku = models.CharField(max_length=25, null= False)
    nombre_articulo = models.CharField(max_length=50, null= False)
    unidad_medida= models.ForeignKey(UnidadesMedida, on_delete=models.RESTRICT, null= False )
    grupo = models.ForeignKey(GruposProveedor, on_delete=models.RESTRICT, null= False )
    linea = models.ForeignKey(LineasArticulos, on_delete=models.RESTRICT, null= False)
    sublinea= models.ForeignKey(SublineasArticulos, on_delete=models.RESTRICT, null= False)
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)
    marca= models.ForeignKey(Marcas, on_delete=models.RESTRICT, null= False)
    class Meta:
        db_table = 'articulos_bonificado'
        ordering =["articulo_bonificado_id"]

    def __str__(self)-> str:
        return '%s - %s - %s' % (self.articulo_bonificado_id, self.codigo_sku, self.nombre_articulo)

class CondicionesVenta(models.Model):
    condicion_venta = models.CharField(max_length=3, primary_key=True)
    descripcion = models.CharField(max_length=100, null= False)
    genera_credito = models.CharField(max_length=1, null= False)

    class Meta:
        db_table = 'condiciones_venta'

    def __str__(self)-> str:
        return '%s - %s ' % (self.condicion_venta,self.genera_credito)

   
class CanalCliente(models.Model):
    canal_cliente_id = models.CharField(max_length=2, primary_key=True, unique=True)
    canal_cliente_descripcion = models.CharField(max_length=150, null= False)
    class Meta:
        db_table = 'canal_cliente'
        ordering =["canal_cliente_id"]
    def __str__(self)-> str:
        return '%s- %s ' % (self.canal_cliente_id,self.canal_cliente_descripcion)



class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True,unique=True)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.RESTRICT, null= False)
    nro_documento = models.CharField(max_length=12,unique=True, null= False)
    nombre_razon_social = models.CharField(max_length=150, null= False)
    direccion = models.CharField(max_length=150, null= False)
    canal_cliente = models.ForeignKey(CanalCliente, on_delete=models.RESTRICT, null= False)

    class Meta:
        db_table = 'clientes'
        ordering =["cliente_id"]

    def __str__(self)-> str:
        return '%s - %s - %s - %s' % (self.cliente_id, self.nro_documento,self.nombre_razon_social,self.canal_cliente)


class TipoPedido(models.Model):
    tipo_pedido_id = models.CharField(max_length=3, primary_key=True,unique=True)
    tipo_pedido_nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipos_pedido'
        ordering =["tipo_pedido_id"]

    def __str__(self)-> str:
        return '%s - %s ' % (self.tipo_pedido_id, self.tipo_pedido_nombre)

class TipoPromocion(models.Model):
    tipo_promocion_id = models.CharField(max_length=3, primary_key=True,unique=True)
    tipo_promocion_nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipos_promocion'
        ordering =["tipo_promocion_id"]

    def __str__(self)-> str:
        return '%s - %s ' % (self.tipo_promocion_id, self.tipo_promocion_nombre)


class Promocion(models.Model):
    promocion_id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tipo_promocion =  models.ForeignKey(TipoPromocion, on_delete=models.RESTRICT, null= False)
    canal_cliente = models.ForeignKey(CanalCliente, on_delete=models.RESTRICT)  
    limite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    articulo_bonificado = models.ForeignKey(ArticulosBonificado, related_name='articulo_bonificado', on_delete=models.CASCADE,null=True, blank=True)
    bonificacion_unidades = models.IntegerField(null=True, blank=True)
    articulo = models.ManyToManyField(Articulos)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'promocion'

    def __str__(self):
        return '%s - %s - %s -%s -%s' % (self.fecha_inicio, self.fecha_fin, self.descuento, self.limite, self.articulo_bonificado)

    
class NotaVenta(models.Model):
    nota_venta_id = models.AutoField(primary_key=True, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT, null= False)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.RESTRICT, null= False)
    nro_pedido = models.CharField(max_length=25, null= False)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    tipo_pedido = models.ForeignKey(TipoPedido, on_delete=models.RESTRICT, null= False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, null= False)
    condicion_venta = models.ForeignKey(CondicionesVenta, on_delete=models.RESTRICT, null= False)
    plazo = models.IntegerField()
    tipo_documento = models.CharField(max_length=20, null= False)
    total_pedido = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    promocion_aplicada = models.ForeignKey(Promocion, null=True, blank=True, on_delete=models.SET_NULL)
    

    class Meta:
        db_table = 'notas_venta'
        ordering =["nota_venta_id"]

    def __str__(self)-> str:
        return '%s - %s - %s' % (self.nota_venta_id, self.nro_pedido, self.fecha_pedido)
    

class ItemNotaVenta(models.Model):
    item_id = models.AutoField(primary_key=True, unique=True)
    nota_venta = models.ForeignKey(NotaVenta, on_delete=models.RESTRICT, null= False)
    nro_item = models.IntegerField()
    articulo = models.ForeignKey(Articulos, on_delete=models.RESTRICT, null= False )
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_item_bruto = models.DecimalField(max_digits=12, decimal_places=2,null= True)
    factor_descuento = models.DecimalField(max_digits=12, decimal_places=3,null= True)
    descuento_unitario = models.DecimalField(max_digits=12, decimal_places=2,null= True)
    total_item = models.DecimalField(max_digits=12, decimal_places=2,null= True)
    promocion_aplicada = models.ForeignKey(Promocion, null=True, blank=True, on_delete=models.SET_NULL)
    es_bonificacion = models.BooleanField(default=False) 

    class Meta:
        db_table = 'items_nota_venta'
        ordering =["item_id"]

    def __str__(self):
        return '%s - %s - %s -%s ' % (self.item_id, self.nro_item, self.precio_unitario, self.cantidad)
    def save(self, *args, **kwargs):
        # Calcula el descuento basado en la promoción aplicada
        if self.promocion_aplicada:
            self.factor_descuento = self.promocion_aplicada.descuento
            self.descuento_unitario = self.precio_unitario * self.cantidad * self.factor_descuento / 100
        else:
            self.factor_descuento = 0
            self.descuento_unitario = 0

        # Calcula los demás campos
        self.total_item_bruto = self.precio_unitario * self.cantidad
        self.total_item = self.total_item_bruto - self.descuento_unitario

        super().save(*args, **kwargs)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, fullname, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, fullname, password, **extra_fields)


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True,null= False)
    fullname = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    objects = UsuarioManager()

    def __str__(self):
        return self.email
        
    class Meta:
        db_table = 'usuario'
           
