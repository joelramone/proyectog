from django.contrib import admin

# Register your models here.

from .models import Ticket, RequestLog, DatosFinancieros

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['fecha_inicio', 'fecha_fin', 'simbolo']

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['url', 'method', 'created_at']

@admin.register(DatosFinancieros)
class DatosFinancierosAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'adj_close', 'volumen']
