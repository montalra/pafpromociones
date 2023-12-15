from django import forms
from .models import Empresa, Sucursal, TipoIdentificacion, Vendedor, GruposProveedor, UnidadesMedida,LineasArticulos,SublineasArticulos,Marcas,Articulos, ArticulosBonificado, CondicionesVenta, TipoPedido, CanalCliente, Cliente,  ItemNotaVenta, NotaVenta, Promocion,TipoPromocion
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['empresa_id','nro_documento', 'razon_social', 'direccion']
        widgets = {
            'empresa_id': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['sucursal_id','nombre_comercial', 'direccion', 'empresa']
        widgets = {
            'sucursal_id': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }

class TipoIdentificacionForm(forms.ModelForm):
    class Meta:
        model = TipoIdentificacion
        fields = ['tipo_identificacion_id','tipo_identificacion_nombre']
        widgets = {
            'tipo_identificacion_id': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_identificacion_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['vendedor_id','vendedor_codigo', 'tipo_identificacion', 'nro_documento', 'nombres',
         'direccion', 'correo_electronico', 'nro_movil', 'empresa']
        widgets = {
            'vendedor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_identificacion': forms.Select(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'nro_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }

class GruposProveedorForm(forms.ModelForm):
    class Meta:
        model = GruposProveedor
        fields = ['grupo_id','codigo_grupo', 'grupo_descripcion', 'empresa', 'activo', 'responsable_grupo']
        widgets = {
            'grupo_id': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'responsable_grupo': forms.Select(attrs={'class': 'form-control'}),
        }

class UnidadesMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedida
        fields = ['unidad_medida_id','unidad_nombre']
        widgets = {
            'unidad_medida_id': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LineasArticulosForm(forms.ModelForm):
    class Meta:
        model = LineasArticulos
        fields = ['codigo_linea', 'linea_descripcion', 'grupo', 'activo', 'responsable_linea']
        widgets = {
            'codigo_linea': forms.TextInput(attrs={'class': 'form-control'}),
            'linea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'activo':  forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'responsable_linea': forms.Select(attrs={'class': 'form-control'}),
        }

class SublineasArticulosForm(forms.ModelForm):
    class Meta:
        model = SublineasArticulos
        fields = ['codigo_sublinea', 'sublinea_descripcion', 'linea', 'estado']
        widgets = {
            'codigo_sublinea': forms.TextInput(attrs={'class': 'form-control'}),
            'sublinea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'linea': forms.Select(attrs={'class': 'form-control'}),
            'estado':  forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = ['marca_id','codigo_marca', 'marca_nombre']
        widgets = {
            'marca_id': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['articulo_id','codigo_sku', 'nombre_articulo', 'unidad_medida','grupo', 'linea', 'sublinea', 'empresa' ,'factor_compra', 'factor_reparto', 'marca']
        widgets = {
            'articulo_id': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_articulo': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'linea': forms.Select(attrs={'class': 'form-control'}),
            'sublinea': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'factor_compra': forms.TextInput(attrs={'class': 'form-control'}),
            'factor_reparto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }
        
class ArticulosBonificadoForm(forms.ModelForm):
    class Meta:
        model = ArticulosBonificado
        fields = ['articulo_bonificado_id','codigo_sku', 'nombre_articulo', 'unidad_medida','grupo', 'linea', 'sublinea', 'empresa', 'marca']
        widgets = {
            'articulo_bonificado_id': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_articulo': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'linea': forms.Select(attrs={'class': 'form-control'}),
            'sublinea': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }
        

class CondicionVentaForm(forms.ModelForm):
    class Meta:
        model = CondicionesVenta
        fields = ['condicion_venta','descripcion', 'genera_credito']
        widgets = {
            'condicion_venta': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'genera_credito': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoPedidoForm(forms.ModelForm):
    class Meta:
        model = TipoPedido
        fields = ['tipo_pedido_id','tipo_pedido_nombre']
        widgets = {
            'tipo_pedido_id': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pedido_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class CanalClienteForm(forms.ModelForm):
    class Meta:
        model = CanalCliente
        fields = ['canal_cliente_id','canal_cliente_descripcion']
        widgets = {
            'canal_cliente_id': forms.TextInput(attrs={'class': 'form-control'}),
            'canal_cliente_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_id','tipo_identificacion','nro_documento','nombre_razon_social','direccion','canal_cliente']
        widgets = {
            'canal_cliente_id': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_identificacion': forms.Select(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'canal_cliente': forms.Select(attrs={'class': 'form-control'}),
        }
class NotaVentaForm(forms.ModelForm):
    class Meta:
        model = NotaVenta
        exclude = ['fecha_pedido']
        fields = ['nota_venta_id','empresa', 'sucursal','nro_pedido', 'fecha_pedido','tipo_pedido', 'cliente', 'condicion_venta', 'plazo', 'tipo_documento', 'total_pedido']
        widgets = {
            'nota_venta_id': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'sucursal': forms.Select(attrs={'class': 'form-control'}),
            'nro_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_pedido': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'tipo_pedido': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'condicion_venta': forms.Select(attrs={'class': 'form-control'}),
            'plazo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'total_pedido': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class ItemNotaVentaForm(forms.ModelForm):

    class Meta:
        model = ItemNotaVenta
        fields = ['item_id','nota_venta', 'nro_item','articulo', 'precio_unitario','cantidad', 'total_item_bruto', 'factor_descuento', 'descuento_unitario', 'total_item', 'promocion_aplicada','es_bonificacion']
        widgets = {
            'item_id': forms.TextInput(attrs={'class': 'form-control'}),
            'nota_venta': forms.Select(attrs={'class': 'form-control'}),
            'nro_item': forms.NumberInput(attrs={'class': 'form-control'}),
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'promocion_aplicada' : forms.Select(attrs={'class': 'form-control'}),
            'total_item_bruto': forms.NumberInput(attrs={'class': 'form-control'}),
            'factor_descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'descuento_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_item': forms.NumberInput(attrs={'class': 'form-control'}),
            'es_bonificacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TipoPromocionForm(forms.ModelForm):
    class Meta:
        model = TipoPromocion
        fields = ['tipo_promocion_id','tipo_promocion_nombre']
        widgets = {
            'tipo_promocion_id': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_promocion_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['titulo', 'fecha_inicio', 'fecha_fin', 'tipo_promocion', 'canal_cliente', 'limite', 'articulo_bonificado', 'bonificacion_unidades', 'articulo', 'descuento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'tipo_promocion': forms.Select(attrs={'class': 'form-control'}),
            'canal_cliente': forms.Select(attrs={'class': 'form-control'}),
            'limite': forms.NumberInput(attrs={'class': 'form-control'}),
            'bonificacion_unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'articulo_bonificado': forms.Select(attrs={'class': 'form-control'}),
            'articulo': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        validators=[EmailValidator(message="Ingrese una dirección de correo electrónico válida.")]
    )
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'fullname', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'fullname': 'Nombre Completo',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        help_texts = {
            'password2': 'Por favor, confirme su contraseña.',
        }

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'fullname']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
        }