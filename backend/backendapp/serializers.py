from rest_framework import serializers
from .models import DatosFinancieros
from .models import RequestLog
from .models  import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta():
        model = Ticket
        fields = "__all__"



class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = '__all__'




class DatosFinancierosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosFinancieros
        fields = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'adj_close', 'volumen']