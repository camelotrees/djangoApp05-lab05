from django.contrib import admin, messages
from django.db.models import F

from .models import Categoria, Cliente, Producto


# Accion personalizada: sube el stock de los productos seleccionados en 20
@admin.action(description="Aumentar stock en 20 unidades")
def aumentar_stock(modeladmin, request, queryset):
    actualizados = queryset.update(stock=F('stock') + 20)
    modeladmin.message_user(
        request,
        f"Se aumento en 20 unidades el stock de {actualizados} producto(s).",
        messages.SUCCESS,
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'pub_date')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    actions = [aumentar_stock]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'email', 'fecha_nacimiento')
    search_fields = ('nombres', 'apellidos', 'dni', 'email')
    ordering = ('apellidos',)