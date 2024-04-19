from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import yfinance as yf
import pandas as pd
from .models import DatosFinancieros
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import DatosFinancierosSerializer
# Create your views here.


class GetMethod(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        data = list(Ticket.objects.all().values())
        return Response(data)

class Ticketview(APIView):
    @swagger_auto_schema(
        request_body=TicketSerializer,
        responses={200: TicketSerializer()},  # Definir la respuesta esperada
    )
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            fecha_inicio = serializer.validated_data.get('fecha_inicio')
            fecha_fin = serializer.validated_data.get('fecha_fin')
            simbolo = serializer.validated_data.get('simbolo')
            
            # Obtener datos financieros
            data = MostrarDatos.DataDownloader(simbolo, fecha_inicio, fecha_fin)
            
            # Verificar si se obtuvieron datos financieros
            if data is not None and not data.empty:
                # Guardar datos financieros en la base de datos
                for fecha, datos_dia in data.iterrows():
                    DatosFinancieros.objects.create(
                        fecha=fecha,
                        apertura=datos_dia['Open'],
                        maximo=datos_dia['High'],
                        minimo=datos_dia['Low'],
                        cierre=datos_dia['Close'],
                        adj_close=datos_dia['Adj Close'],
                        volumen=datos_dia['Volume']
                    )
                
                # Devolver respuesta exitosa
                return Response({'message': 'Datos financieros guardados correctamente'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No se pudieron obtener los datos financieros'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

class RequestLogView(APIView):
    @swagger_auto_schema(
        responses={200: RequestLogSerializer(many=True)},
        operation_summary="Get request logs",
        operation_description="Get a list of request logs",
    )
    def get(self, request, format=None):
        logs = RequestLog.objects.all()
        serializer = RequestLogSerializer(logs, many=True)
        return Response(serializer.data)

#muestra la tabla con los datos pedidos a yfinance
class MostrarDatos:
    @staticmethod
    def DataDownloader(simbolo,fecha_inicio, fecha_fin):
        data = yf.download(simbolo, start=fecha_inicio, end=fecha_fin)
        return data
    
class MyAPIView(APIView):
    def get(self, request, format=None):
        data = {'example': 'data'}
        print(data)  # Imprimir los datos en la consola del servidor
        return Response(data)
    
#guarda los datos obtenidos con la clase MostrarDatos
@api_view(['POST'])
def procesar_y_guardar_datos(request):
    # Obtener los datos del formulario enviado desde el frontend
    simbolo = request.data.get('simbolo')
    fecha_inicio = request.data.get('fecha_inicio')
    fecha_fin = request.data.get('fecha_fin')

    # Llama a la clase MostrarDatos para obtener los datos
    datos = MostrarDatos.DataDownloader(simbolo, fecha_inicio, fecha_fin)

    # Verifica si se obtuvieron datos y procede a guardarlos
    if datos is not None:
        # Itera sobre los datos y guárdalos en la base de datos
        for fecha, datos_dia in datos.iterrows():
            DatosFinancieros.objects.create(
                fecha=fecha,
                apertura=datos_dia['Open'],
                maximo=datos_dia['High'],
                minimo=datos_dia['Low'],
                cierre=datos_dia['Close'],
                adj_close=datos_dia['Adj Close'],
                volumen=datos_dia['Volume']
                # Otros campos según tu modelo
            )
        
        return Response({'message': 'Datos financieros guardados exitosamente'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'No se pudieron obtener los datos financieros'}, status=status.HTTP_400_BAD_REQUEST)

#muestra los datos
def mostrar_datos_financieros(request):
    datos = DatosFinancieros.objects.all()
    for dato in datos:
        print("Fecha:", dato.fecha)
        print("Apertura:", dato.apertura)
        print("maximo:", dato.maximo)
        print("minimo:", dato.minimo)
        print("cierre:", dato.cierre)
        print("adj_close:", dato.adj_close)
        print("volumen:", dato.volumen)
        # Agrega más campos según sea necesario
    return render(request, 'formulario.html', {'datos': datos})

class DatosFinancierosListView(APIView):
    def get(self, request, format=None):
        # Consulta los datos financieros de la base de datos
        datos_financieros = DatosFinancieros.objects.all()

        # Serializa los datos financieros en el formato deseado
        serializer = DatosFinancierosSerializer(datos_financieros, many=True)

        # Devuelve la respuesta JSON con los datos financieros
        return Response(serializer.data)