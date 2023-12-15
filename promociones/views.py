from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa,Sucursal,TipoIdentificacion, Vendedor,GruposProveedor, UnidadesMedida, LineasArticulos,SublineasArticulos,Marcas, Articulos,  ArticulosBonificado, CondicionesVenta, TipoPedido,CanalCliente,Cliente,NotaVenta, ItemNotaVenta, Promocion, TipoPromocion
from .forms import LoginForm, EmpresaForm,SucursalForm, TipoIdentificacionForm, VendedorForm,GruposProveedorForm, UnidadesMedidaForm,  LineasArticulosForm, SublineasArticulosForm, MarcasForm, ArticulosForm,ArticulosBonificadoForm,CondicionVentaForm,TipoPedidoForm, CanalClienteForm,ClienteForm, NotaVentaForm,ItemNotaVentaForm, UsuarioForm,UsuarioUpdateForm,Usuario,PromocionForm, TipoPromocionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid Email or Password')
        else:
            messages.error(request, 'Invalid Form Submission')
    
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

#INDEX

def index(request):
   return render(request, 'index/index.html')

#EMPRESA

def EmpresaLista(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/empresa_lista.html', {'object_list': empresas})

def EmpresaRegistro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_lista')
    else:
        form = EmpresaForm()

    return render(request, 'empresa/nuevo_empresa.html', {'form': form})

def EmpresaActualizar(request, empresa_id):
    empresa = Empresa.objects.get(empresa_id=empresa_id)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_lista')
    else:
        form = EmpresaForm(instance=empresa)

    return render(request, 'empresa/nuevo_empresa.html', {'form': form})

def EmpresaEliminar(request, empresa_id):
    empresa = get_object_or_404(Empresa, empresa_id=empresa_id)   
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_lista')
    else:
        return render(request, 'empresa/empresa_eliminar.html', {'empresa': empresa})

#SUCURSAL

def SucursalLista(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/sucursal_lista.html', {'object_list': sucursales})

def SucursalRegistro(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucursal_lista')
    else:
        form = SucursalForm()

    return render(request, 'sucursal/nuevo_sucursal.html', {'form': form})

def SucursalActualizar(request, sucursal_id):
    sucursal = Sucursal.objects.get(sucursal_id=sucursal_id)

    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('sucursal_lista')
    else:
        form = SucursalForm(instance=sucursal)

    return render(request, 'sucursal/nuevo_sucursal.html', {'form': form})

def SucursalEliminar(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, sucursal_id=sucursal_id)   
    if request.method == 'POST':
        sucursal.delete()
        return redirect('sucursal_lista')
    else:
        return render(request, 'sucursal/sucursal_eliminar.html', {'sucursal':sucursal})

#TIPO DE IDENTIFICACION

def TipoIdentificacionLista(request):
    tipo_identificaciones = TipoIdentificacion.objects.all()
    return render(request, 'tipoidentificacion/tipoidentificacion_lista.html', {'object_list': tipo_identificaciones})

def TipoIdentificacionRegistro(request):
    if request.method == 'POST':
        form = TipoIdentificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipoidentificacion_lista')
    else:
        form = TipoIdentificacionForm()

    return render(request, 'tipoidentificacion/nuevo_tipoidentificacion.html', {'form': form})

def TipoIdentificacionActualizar(request, tipo_identificacion_id):
    tipoidentificacion = TipoIdentificacion.objects.get(tipo_identificacion_id=tipo_identificacion_id)

    if request.method == 'POST':
        form = TipoIdentificacionForm(request.POST, instance=tipoidentificacion)
        if form.is_valid():
            form.save()
            return redirect('tipoidentificacion_lista')
    else:
        form = TipoIdentificacionForm(instance=tipoidentificacion)

    return render(request, 'tipoidentificacion/nuevo_tipoidentificacion.html', {'form': form})

def TipoIdentificacionEliminar(request, tipo_identificacion_id):
    tipoidentificacion = get_object_or_404(TipoIdentificacion, tipo_identificacion_id=tipo_identificacion_id)   
    if request.method == 'POST':
        tipoidentificacion.delete()
        return redirect('tipoidentificacion_lista')
    else:
        return render(request, 'tipoidentificacion/tipoidentificacion_eliminar.html', {'tipoidentificacion':tipoidentificacion})    

#VENDEDOR
def VendedorLista(request):
    Vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/vendedor_lista.html', {'object_list': Vendedores})

def VendedorRegistro(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_lista')
    else:
        form = VendedorForm()

    return render(request, 'vendedor/nuevo_vendedor.html', {'form': form})

def VendedorActualizar(request, vendedor_id):
    vendedor = Vendedor.objects.get(vendedor_id=vendedor_id)

    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor_lista')
    else:
        form = VendedorForm(instance=vendedor)

    return render(request, 'vendedor/nuevo_vendedor.html', {'form': form})

def VendedorEliminar(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, vendedor_id=vendedor_id)   
    if request.method == 'POST':
        vendedor.delete()
        return redirect('vendedor_lista')
    else:
        return render(request, 'vendedor/vendedor_eliminar.html', {'vendedor':vendedor})

#GRUPO PROVEEDOR
def GruposProveedorLista(request):
    GruposProveedores = GruposProveedor.objects.all()
    return render(request, 'gruposproveedor/grupos_proveedor_lista.html', {'object_list': GruposProveedores})


def GruposProveedorRegistro(request):
    if request.method == 'POST':
        form = GruposProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupos_proveedor_lista')
    else:
        form = GruposProveedorForm()

    return render(request, 'gruposproveedor/nuevo_grupos_proveedor.html', {'form': form})

def GruposProveedorActualizar(request, grupo_id):
    gruposproveedor = GruposProveedor.objects.get(grupo_id=grupo_id)

    if request.method == 'POST':
        form = GruposProveedorForm(request.POST, instance=gruposproveedor)
        if form.is_valid():
            form.save()
            return redirect('grupos_proveedor_lista')
    else:
        form = GruposProveedorForm(instance=gruposproveedor)

    return render(request, 'gruposproveedor/nuevo_grupos_proveedor.html', {'form': form})

def GruposProveedorEliminar(request, grupo_id):
    gruposproveedor = get_object_or_404(GruposProveedor, grupo_id=grupo_id)   
    if request.method == 'POST':
        gruposproveedor.delete()
        return redirect('grupos_proveedor_lista')
    else:
        return render(request, 'gruposproveedor/grupos_proveedor_eliminar.html', {'gruposproveedor':gruposproveedor})

#UNIDAD

def UnidadesMedidaLista(request):
    UnidadesMedidas = UnidadesMedida.objects.all()
    return render(request, 'unidadesmedida/unidades_medida_lista.html', {'object_list': UnidadesMedidas})

def UnidadesMedidaRegistro(request):
    if request.method == 'POST':
        form = UnidadesMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidades_medida_lista')
    else:
        form = UnidadesMedidaForm()

    return render(request, 'unidadesmedida/nuevo_unidades_medida.html', {'form': form})

def UnidadesMedidaActualizar(request, unidad_medida_id):
    unidadesmedida = get_object_or_404(UnidadesMedida, unidad_medida_id=unidad_medida_id)

    if request.method == 'POST':
        form = UnidadesMedidaForm(request.POST, instance=unidadesmedida)
        if form.is_valid():
            form.save()
            return redirect('unidades_medida_lista')
    else:
        form = UnidadesMedidaForm(instance=unidadesmedida)

    return render(request, 'unidadesmedida/nuevo_unidades_medida.html', {'form': form})

def UnidadesMedidaEliminar(request, unidad_medida_id):
    unidadesmedida = get_object_or_404(UnidadesMedida, id=unidad_medida_id)   
    if request.method == 'POST':
        unidadesmedida.delete()
        return redirect('unidades_medida_lista')
    else:
        return render(request, 'unidadesmedida/unidades_medida_eliminar.html', {'unidadesmedida':unidadesmedida})


#LINEASARTICULOS

def LineasArticulosLista(request):
    lineas_articulos = LineasArticulos.objects.all()
    return render(request, 'lineasArticulos/lineasArticulos_lista.html', {'object_list': lineas_articulos})

def LineasArticulosRegistro(request):
    if request.method == 'POST':
        form = LineasArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lineasArticulos_lista')
    else:
        form = LineasArticulosForm()

    return render(request, 'lineasArticulos/nuevo_lineasArticulos.html', {'form': form})

def LineasArticulosActualizar(request, linea_id):
    lineas_articulo = get_object_or_404(LineasArticulos, linea_id=linea_id)

    if request.method == 'POST':
        form = LineasArticulosForm(request.POST, instance=lineas_articulo)
        if form.is_valid():
            form.save()
            return redirect('lineasArticulos_lista')
    else:
        form = LineasArticulosForm(instance=lineas_articulo)

    return render(request, 'lineasArticulos/nuevo_lineasArticulos.html', {'form': form})

def LineasArticulosEliminar(request, linea_id):
    lineas_articulo = get_object_or_404(LineasArticulos, linea_id=linea_id)
    
    if request.method == 'POST':
        lineas_articulo.delete()
        return redirect('lineasArticulos_lista')
    else:
        return render(request, 'lineasArticulos/lineasArticulos_eliminar.html', {'linea': lineas_articulo})

#SUBLINEASARTICULOS

def SublineasArticulosLista(request):
    sublineas_articulos = SublineasArticulos.objects.all()
    return render(request, 'sublineasArticulos/sublineasArticulos_lista.html', {'object_list': sublineas_articulos})

def SublineasArticulosRegistro(request):
    if request.method == 'POST':
        form = SublineasArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sublineasArticulos_lista')
    else:
        form = SublineasArticulosForm()

    return render(request, 'sublineasArticulos/nuevo_sublineasArticulos.html', {'form': form})

def SublineasArticulosActualizar(request, sublinea_id):
    sublinea = get_object_or_404(SublineasArticulos, sublinea_id=sublinea_id)

    if request.method == 'POST':
        form = SublineasArticulosForm(request.POST, instance=sublinea)
        if form.is_valid():
            form.save()
            return redirect('sublineasArticulos_lista')
    else:
        form = SublineasArticulosForm(instance=sublinea)

    return render(request, 'sublineasArticulos/nuevo_sublineasArticulos.html', {'form': form})

def SublineasArticulosEliminar(request, sublinea_id):
    sublinea = get_object_or_404(SublineasArticulos, sublinea_id=sublinea_id)
    
    if request.method == 'POST':
        sublinea.delete()
        return redirect('sublineasArticulos_lista')
    else:
        return render(request, 'sublineasArticulos/sublineasArticulos_eliminar.html', {'sublinea': sublinea})

#Marcas
def MarcasLista(request):
    marcas = Marcas.objects.all()
    return render(request, 'marcas/marcas_lista.html', {'object_list': marcas})

def MarcasRegistro(request):
    if request.method == 'POST':
        form = MarcasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcas_lista')
    else:
        form = MarcasForm()

    return render(request, 'marcas/nuevo_marcas.html', {'form': form})

def MarcasActualizar(request, marca_id):
    marca = Marcas.objects.get(marca_id=marca_id)

    if request.method == 'POST':
        form = MarcasForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marcas_lista')
    else:
        form = MarcasForm(instance=marca)

    return render(request, 'marcas/nuevo_marcas.html', {'form': form})

def MarcasEliminar(request, marca_id):
    marca = get_object_or_404(Marcas, marca_id= marca_id)   
    if request.method == 'POST':
        marca.delete()
        return redirect('marcas_lista')
    else:
        return render(request, 'marcas/marcas_eliminar.html', {'marcas':marca})

#ARTICULOS
def ArticulosLista(request):
    articulos = Articulos.objects.all()
    return render(request, 'articulos/articulos_lista.html', {'object_list': articulos})

def ArticulosRegistro(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = ArticulosForm()

    return render(request, 'articulos/nuevo_articulos.html', {'form': form})

def ArticulosActualizar(request, articulo_id):
    articulo = Articulos.objects.get(articulo_id=articulo_id)

    if request.method == 'POST':
        form = ArticulosForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = ArticulosForm(instance=articulo)

    return render(request, 'articulos/nuevo_articulos.html', {'form': form})

def ArticulosEliminar(request, articulo_id):
    articulo = get_object_or_404(Articulos, articulo_id=articulo_id)   
    if request.method == 'POST':
        articulo.delete()
        return redirect('articulos_lista')
    else:
        return render(request, 'articulos/articulos_eliminar.html', {'articulo':articulo}) 
     
#ArticulosBonificado
def ArticulosBonificadoLista(request):
    articulosbonificado = ArticulosBonificado.objects.all()
    return render(request, 'articulosbonificado/articulosbonificado_lista.html', {'object_list': articulosbonificado})

def ArticulosBonificadoRegistro(request):
    if request.method == 'POST':
        form = ArticulosBonificadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulosbonificado_lista')
    else:
        form = ArticulosBonificadoForm()

    return render(request, 'articulosbonificado/nuevo_articulosbonificado.html', {'form': form})

def ArticulosBonificadoActualizar(request, articulo_bonificado_id):
    articulobonificado = Articulos.objects.get(articulo_bonificado_id=articulo_bonificado_id)

    if request.method == 'POST':
        form = ArticulosBonificadoForm(request.POST, instance=articulobonificado)
        if form.is_valid():
            form.save()
            return redirect('articulosbonificado_lista')
    else:
        form = ArticulosBonificadoForm(instance=articulobonificado)

    return render(request, 'articulosbonificado/nuevo_articulosbonificado.html', {'form': form})

def ArticulosBonificadoEliminar(request, articulo_bonificado_id):
    articulobonificado = get_object_or_404(ArticulosBonificado, articulo_bonificado_id=articulo_bonificado_id)   
    if request.method == 'POST':
        articulobonificado.delete()
        return redirect('articulosbonificado_lista')
    else:
        return render(request, 'articulosbonificado/articulosbonificado_eliminar.html', {'articulo':articulobonificado}) 
     

#CONDICION DE VENTA

def CondicionVentaLista(request):
    condicionesventas = CondicionesVenta.objects.all()
    return render(request, 'condicionesventa/cventa_lista.html', {'object_list': condicionesventas})

def CondicionVentaRegistro(request):
    if request.method == 'POST':
        form = CondicionVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cventa_lista') 
    else:
        form = CondicionVentaForm()

    return render(request, 'condicionesventa/nuevo_cventa.html', {'form': form})

def CondicionVentaActualizar(request, condicion_venta):
    condicionesventa = get_object_or_404(CondicionesVenta, condicion_venta=condicion_venta)

    if request.method == 'POST':
        form = CondicionVentaForm(request.POST, instance=condicionesventa)
        if form.is_valid():
            form.save()
            return redirect('cventa_lista')  
    else:
        form = CondicionVentaForm(instance=condicionesventa)

    return render(request, 'condicionesventa/nuevo_cventa.html', {'form': form})

def CondicionVentaEliminar(request, condicion_venta):
    condicionesventa = get_object_or_404(CondicionesVenta, condicion_venta=condicion_venta)   
    if request.method == 'POST':
        condicionesventa.delete()
        return redirect('cventa_lista')  
    else:
        return render(request, 'condicionesventa/cventa_eliminar.html', {'condicionventa': condicionesventa})
    
#TipoPedido
def TipoPedidoLista(request):
    tipopedido = TipoPedido.objects.all()
    return render(request, 'tipopedido/tipopedido_lista.html', {'object_list': tipopedido})

def TipoPedidoRegistro(request):
    if request.method == 'POST':
        form = TipoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipopedido_lista')
    else:
        form = TipoPedidoForm()

    return render(request, 'tipopedido/nuevo_tipopedido.html', {'form': form})

def TipoPedidoActualizar(request, tipo_pedido_id):
    tipopedido = TipoPedido.objects.get(tipo_pedido_id=tipo_pedido_id)

    if request.method == 'POST':
        form = TipoPedidoForm(request.POST, instance=tipopedido)
        if form.is_valid():
            form.save()
            return redirect('tipopedido_lista')
    else:
        form = TipoPedidoForm(instance=tipopedido)

    return render(request, 'tipopedido/nuevo_tipopedido.html', {'form': form})

def TipoPedidoEliminar(request, tipo_pedido_id):
    tipopedido = get_object_or_404(TipoPedido, tipo_pedido_id=tipo_pedido_id)   
    if request.method == 'POST':
        tipopedido.delete()
        return redirect('tipopedido_lista')
    else:
        return render(request, 'tipopedido/tipopedido_eliminar.html', {'tipopedido':tipopedido}) 
    

#CanalCliente
def CanalClienteLista(request):
    canalclientes = CanalCliente.objects.all()
    return render(request, 'canalcliente/canalcliente_lista.html', {'object_list': canalclientes})

def CanalClienteRegistro(request):
    if request.method == 'POST':
        form = CanalClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('canalcliente_lista')
    else:
        form = CanalClienteForm()

    return render(request, 'canalcliente/nuevo_canalcliente.html', {'form': form})

def CanalClienteActualizar(request, canal_cliente_id):
    canalcliente = CanalCliente.objects.get(canal_cliente_id=canal_cliente_id)

    if request.method == 'POST':
        form = CanalClienteForm(request.POST, instance=canalcliente)
        if form.is_valid():
            form.save()
            return redirect('canalcliente_lista')
    else:
        form = CanalClienteForm(instance=canalcliente)

    return render(request, 'canalcliente/nuevo_canalcliente.html', {'form': form})

def CanalClienteEliminar(request, canal_cliente_id):
    canalcliente = get_object_or_404(CanalCliente, canal_cliente_id=canal_cliente_id)   
    if request.method == 'POST':
        canalcliente.delete()
        return redirect('canalcliente_lista')
    else:
        return render(request, 'canalcliente/canalcliente_eliminar.html', {'canalcliente':canalcliente})
    
#Cliente
def ClienteLista(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_lista.html', {'object_list': clientes})

def ClienteRegistro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm()

    return render(request, 'cliente/nuevo_cliente.html', {'form': form})

def ClienteActualizar(request, cliente_id):
    cliente = Cliente.objects.get(cliente_id=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'cliente/nuevo_cliente.html', {'form': form})

def ClienteEliminar(request, cliente_id):
    cliente = get_object_or_404(Cliente, cliente_id= cliente_id)   
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    else:
        return render(request, 'cliente/cliente_eliminar.html', {'cliente':cliente})
    
#NotaVenta
def NotaVentaLista(request):
    notaventa = NotaVenta.objects.all()
    return render(request, 'notaventa/notaventa_lista.html', {'object_list': notaventa})

def NotaVentaRegistro(request):
    if request.method == 'POST':
        form = NotaVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notaventa_lista')
    else:
        form = NotaVentaForm()

    return render(request, 'notaventa/nuevo_notaventa.html', {'form': form})

def NotaVentaActualizar(request, nota_venta_id):
    notaventa = NotaVenta.objects.get(nota_venta_id=nota_venta_id)

    if request.method == 'POST':
        form = NotaVentaForm(request.POST, instance=notaventa)
        if form.is_valid():
            form.save()
            return redirect('notaventa_lista')
    else:
        form = NotaVentaForm(instance=notaventa)

    return render(request, 'notaventa/nuevo_notaventa.html', {'form': form})

def NotaVentaEliminar(request, nota_venta_id):
    notaventa = get_object_or_404(NotaVenta, nota_venta_id=nota_venta_id)   
    if request.method == 'POST':
        notaventa.delete()
        return redirect('nuevo_itemnotaventa')
    else:
        return render(request, 'notaventa/notaventa_eliminar.html', {'notaventa':notaventa})    
#ItemNotaVenta

def ItemNotaVentaDetalle(request,item_id):
    itemnotaventa = get_object_or_404(ItemNotaVenta, item_id=item_id)   
    return render(request, 'itemnotaventa/itemnotaventa_detalle.html', {'itemnotaventa':itemnotaventa})

def ItemNotaVentaRegistro(request):
    itemnotaventa = ItemNotaVenta.objects.all()
    
    if request.method == 'POST':
        form = ItemNotaVentaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('nuevo_itemnotaventa')
    else:
        form = ItemNotaVentaForm()

    return render(request, 'itemnotaventa/nuevo_itemnotaventa.html', {'object_list': itemnotaventa, 'form': form})

def ItemNotaVentaActualizar(request, item_id):
    itemnotaventa = ItemNotaVenta.objects.get(item_id=item_id)

    if request.method == 'POST':
        form = ItemNotaVentaForm(request.POST, instance=itemnotaventa)
        if form.is_valid():
            form.save()  
            return redirect('nuevo_itemnotaventa')
    else:
        form = ItemNotaVentaForm(instance=itemnotaventa)

    return render(request, 'itemnotaventa/itemnotaventa_actualizar.html', {'form': form})
def ItemNotaVentaEliminar(request, item_id):
    itemnotaventa = get_object_or_404(ItemNotaVenta, item_id=item_id)   
    if request.method == 'POST':
        itemnotaventa.delete()
        return redirect('nuevo_itemnotaventa')
    else:
        return render(request, 'itemnotaventa/itemnotaventa_eliminar.html', {'itemnotaventa':itemnotaventa}) 

#Tipo Promocion
def TipoPromocionLista(request):
    tipopromociones = TipoPromocion.objects.all()
    return render(request, 'tipopromocion/tipopromocion_lista.html', {'object_list': tipopromociones})

def TipoPromocionRegistro(request):
    if request.method == 'POST':
        form = TipoPromocionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipopromocion_lista')
    else:
        form = TipoPromocionForm()

    return render(request, 'tipopromocion/nuevo_tipopromocion.html', {'form': form})

def TipoPromocionActualizar(request, tipo_promocion_id):
    tipo_promocion = TipoPromocion.objects.get(tipo_promocion_id=tipo_promocion_id)

    if request.method == 'POST':
        form = TipoPromocionForm(request.POST, instance=tipo_promocion)
        if form.is_valid():
            form.save()
            return redirect('tipopromocion_lista')
    else:
        form = TipoPromocionForm(instance=tipo_promocion)

    return render(request, 'tipopromocion/nuevo_tipopromocion.html', {'form': form})

def TipoPromocionEliminar(request, tipo_promocion_id):
    tipo_promocion = get_object_or_404(TipoPromocion, tipo_promocion_id=tipo_promocion_id)   
    if request.method == 'POST':
        tipo_promocion.delete()
        return redirect('tipopromocion_lista')
    else:
        return render(request, 'tipopromocion/tipopromocion_eliminar.html', {'tipo_promocion': tipo_promocion})

#Promociones

def PromocionDetalle(request, promocion_id):
    promocion = get_object_or_404(Promocion, promocion_id=promocion_id)
    return render(request, 'promocion/promocion_detalle.html', {'promocion': promocion})

def PromocionRegistro(request):
    promociones = Promocion.objects.all()
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            promocion = form.save(commit=False)
            promocion.save()

            articulos_seleccionados = request.POST.getlist('articulo')
            promocion.articulo.set(articulos_seleccionados)

            promocion.save()

            return redirect('nuevo_promocion')
    else:
        form = PromocionForm()

    return render(request, 'promocion/nuevo_promocion.html', {'object_list': promociones, 'form': form})


def PromocionActualizar(request, promocion_id):
    promocion = Promocion.objects.get(promocion_id=promocion_id)

    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('nuevo_promocion')
    else:
        form = PromocionForm(instance=promocion)

    return render(request, 'promocion/promocion_actualizar .html', {'form': form})

def PromocionEliminar(request, promocion_id):
    promocion = get_object_or_404(Promocion, promocion_id=promocion_id)
    if request.method == 'POST':
        promocion.delete()
        return redirect('nuevo_promocion')
    return render(request, 'promocion/promocion_eliminar.html', {'promocion': promocion})


#Usuarios
def UsuarioLista(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/usuario_lista.html', {'object_list': usuarios})

def UsuarioRegistro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            usuario =authenticate(email=email, username= username,password=password)
            login(request, user)
            return redirect('usuario_lista')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/nuevo_usuario.html', {'form': form})

def UsuarioActualizar(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_lista')
    else:
        form = UsuarioUpdateForm(instance=usuario)
    return render(request, 'usuario/usuario_actualizar.html', {'form': form, 'usuario': usuario})

def UsuarioEliminar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_lista')
    return render(request, 'usuario/usuario_eliminar.html', {'usuario': usuario})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('login')
    return render(request, 'cerrar/logout.html')
   

