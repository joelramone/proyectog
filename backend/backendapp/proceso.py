import pandas as pd 
import numpy as np
import plotly
import yfinance as yf

#defino variables

fecha_inicio = 'None'
fecha_fin = 'None'
simbolo = []

class MostrarDatos():
    def DataDownloader():
        data = yf.download(simbolo,start=fecha_inicio,end=fecha_fin)
        return data
    
        
