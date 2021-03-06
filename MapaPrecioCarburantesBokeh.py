# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:41:40 2022

@author: jlluch
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:07:29 2022

@author: jlluch
"""
import pandas as pd
import dataframe_image as dfi
import tweepy
from tweepy import OAuthHandler  
import folium
from folium.plugins import HeatMap
from os import system
from bokeh.plotting import figure, output_file, show

   
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

prov = ['ALBACETE','ALICANTE','ALMERÍA','ARABA/ÁLAVA','ASTURIAS','ÁVILA','BADAJOZ','BALEARS (ILLES)','BARCELONA','BIZKAIA','BURGOS','CÁCERES','CÁDIZ','CANTABRIA','CASTELLÓN / CASTELLÓ','CIUDAD REAL','CÓRDOBA','CORUÑA (A)','CUENCA','GIPUZKOA','GIRONA','GRANADA','GUADALAJARA','HUELVA','HUESCA','JAÉN','LEÓN','LLEIDA','LUGO'
'MADRID','MÁLAGA','MURCIA','NAVARRA','OURENSE','PALENCIA','PONTEVEDRA','RIOJA (LA)','SALAMANCA','SEGOVIA','SEVILLA','SORIA','TARRAGONA','TERUEL','TOLEDO','VALENCIA / VALÈNCIA','VALLADOLID','ZAMORA','ZARAGOZA']
path = 'C:\Temp\PrecioCarburantes\\'

URL = "https://geoportalgasolineras.es/resources/files/preciosEESS_es.xls"
df = pd.read_excel(URL, skiprows=3, engine="xlrd")
# Provincia	Municipio	Localidad	Código postal	Dirección	Margen	Longitud	Latitud	Toma de datos	
# Precio gasolina 95 E5	Precio gasolina 95 E10	Precio gasolina 95 E5 Premium	Precio gasolina 98 E5	Precio gasolina 98 E10	Precio gasóleo A	Precio gasóleo Premium	Precio gasóleo B	Precio gasóleo C	Precio bioetanol	% bioalcohol	Precio biodiésel	% éster metílico	Precio gases licuados del petróleo	Precio gas natural comprimido	Precio gas natural licuado	Precio hidrógeno	Rótulo	Tipo venta	Rem.	Horario	Tipo servicio

path = 'C:\\Users\jlluch\Documents\GitHub\jlluch.github.io\\'

elim = ['MELILLA','CEUTA','PALMAS (LAS)','SANTA CRUZ DE TENERIFE']
df = df[~df.Provincia.isin(elim)] 
cols = ['Precio gasolina 95 E5','Precio gasóleo A','Longitud','Latitud']
df[cols]=df[cols].replace(',','.',regex=True).astype(float)

campo = 'Precio gasolina 95 E5'
stats = df.groupby('Provincia')[campo].mean().reset_index()
#x=stats.Provincia.tolist()
x = list(range(1,len(stats)))
top=stats[campo].tolist()

p = figure(width=800,height=400)
p.vbar(
    x = x,
    top = top,
    width=0.5,
    bottom=0,
    color="firebrick",
)

show(p)


# medlat=df.Latitud.mean()
# medlon=df.Longitud.mean()

# hmap = folium.Map(location=[medlat,medlon],zoom_start=8,tiles='stamenterrain',attr='LOL',max_bounds=True,min_zoom=6.5)

# # prov = df.Provincia.drop_duplicates().tolist()
# # prov = ['VALENCIA / VALÈNCIA']
# ic = 'certificate'
# rus = 100
# for p in prov:
    
#    dfaux = df[df.Provincia==p]
#    dfaux = dfaux.dropna(subset=['Precio gasolina 95 E5'])
#    maxim = dfaux['Precio gasolina 95 E5'].max()
#    minim = dfaux['Precio gasolina 95 E5'].min()
#    dif = maxim-minim
#    for i in range(len(dfaux)):
#        pr = dfaux['Precio gasolina 95 E5'].iat[i]
#        norm = (pr-minim)/dif
#        color = '#'+rgb_to_hex((int(norm*255),int((1.0-norm)*255),0))
#        data = str(dfaux.Localidad.iat[i])+"\n"+str(dfaux.Dirección.iat[i])+"\nGas 95: "+str(pr)+"€"+"\nDiesel: "+str(dfaux['Precio gasóleo A'].iat[i])+"€"
#        folium.Circle(location=[dfaux.Latitud.iat[i],dfaux.Longitud.iat[i],],popup=data,radius=rus,color=color,fill=True, fill_opacity=0.7).add_to(hmap)

# hmap.save(path+'index.html')
