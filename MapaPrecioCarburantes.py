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


   
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

prov = ['ALBACETE','ALICANTE','ALMERÍA','ARABA/ÁLAVA','ASTURIAS','ÁVILA','BADAJOZ','BALEARS (ILLES)','BARCELONA','BIZKAIA','BURGOS','CÁCERES','CÁDIZ','CANTABRIA','CASTELLÓN / CASTELLÓ','CIUDAD REAL','CÓRDOBA','CORUÑA (A)','CUENCA','GIPUZKOA','GIRONA','GRANADA','GUADALAJARA','HUELVA','HUESCA','JAÉN','LEÓN','LLEIDA','LUGO',
'MADRID','MÁLAGA','MURCIA','NAVARRA','OURENSE','PALENCIA','PONTEVEDRA','RIOJA (LA)','SALAMANCA','SEGOVIA','SEVILLA','SORIA','TARRAGONA','TERUEL','TOLEDO','VALENCIA / VALÈNCIA','VALLADOLID','ZAMORA','ZARAGOZA','MELILLA','CEUTA','PALMAS (LAS)','SANTA CRUZ DE TENERIFE']
path = 'C:\Temp\PrecioCarburantes\\'

URL = "https://geoportalgasolineras.es/resources/files/preciosEESS_es.xls"
df = pd.read_excel(URL, skiprows=3, engine="xlrd")
# Provincia	Municipio	Localidad	Código postal	Dirección	Margen	Longitud	Latitud	Toma de datos	
# Precio gasolina 95 E5	Precio gasolina 95 E10	Precio gasolina 95 E5 Premium	Precio gasolina 98 E5	Precio gasolina 98 E10	Precio gasóleo A	Precio gasóleo Premium	Precio gasóleo B	Precio gasóleo C	Precio bioetanol	% bioalcohol	Precio biodiésel	% éster metílico	Precio gases licuados del petróleo	Precio gas natural comprimido	Precio gas natural licuado	Precio hidrógeno	Rótulo	Tipo venta	Rem.	Horario	Tipo servicio

path = 'C:\\Users\jlluch\Documents\GitHub\jlluch.github.io\\'

elim = ['MELILLA','CEUTA','PALMAS (LAS)','SANTA CRUZ DE TENERIFE']
# df = df[~df.Provincia.isin(elim)] 
cols = ['Precio gasolina 95 E5','Precio gasóleo A','Longitud','Latitud']
df[cols]=df[cols].replace(',','.',regex=True).astype(float)
df = df[~df['Dirección'].str.contains('CARRETERA VICALVARO A ESTACION DE')]
#df.iat[6822,4]='CARRETERA VICALVARO KM. 22'

medlat=df.Latitud.mean()
medlon=df.Longitud.mean()

hmap = folium.Map(location=[medlat,medlon],zoom_start=8,tiles='stamenterrain',attr='LOL',max_bounds=True,min_zoom=6.5)

# prov = df.Provincia.drop_duplicates().tolist()
# prov = ['VALENCIA / VALÈNCIA']
ic = 'certificate'
rus = 100
for p in prov:
   print(p) 
   dfaux = df[df.Provincia==p]
   dfaux = dfaux.dropna(subset=['Precio gasolina 95 E5'])
   
   print(len(dfaux))
   maxim = dfaux['Precio gasolina 95 E5'].max()
   minim = dfaux['Precio gasolina 95 E5'].min()
   dif = maxim-minim
   for i in range(len(dfaux)):
       pr = dfaux['Precio gasolina 95 E5'].iat[i]
       norm = (pr-minim)/dif
       color = '#'+rgb_to_hex((int(norm*255),int((1.0-norm)*255),0))
       data = str(dfaux.Localidad.iat[i])+"\n"+str(dfaux.Dirección.iat[i])+"\nGas 95: "+str(pr)+"€"+"\nDiesel: "+str(dfaux['Precio gasóleo A'].iat[i])+"€"
       folium.Circle(location=[dfaux.Latitud.iat[i],dfaux.Longitud.iat[i],],popup=data,radius=rus,color=color,fill=True, fill_opacity=0.7).add_to(hmap)

       
   dfaux2 = df[df.Provincia==p]
   dfaux2 = dfaux2.dropna(subset=['Precio gasóleo A'])
   dfaux2 = dfaux2[dfaux2['Precio gasolina 95 E5'].isnull()]
   print(len(dfaux2))
   maxim = dfaux2['Precio gasóleo A'].max()
   minim = dfaux2['Precio gasóleo A'].min()
   dif = maxim-minim
   if (len(dfaux2)>0):
        for i in range(len(dfaux2)):
            pr = dfaux2['Precio gasóleo A'].iat[i]
            norm = (pr-minim)/dif
            color = '#'+rgb_to_hex((int(norm*255),int((1.0-norm)*255),0))
            data = str(dfaux2.Localidad.iat[i])+"\n"+str(dfaux2.Dirección.iat[i])+"\nGas 95: "+str(pr)+"€"+"\nDiesel: "+str(dfaux2['Precio gasóleo A'].iat[i])+"€"
            folium.Circle(location=[dfaux2.Latitud.iat[i],dfaux2.Longitud.iat[i],],popup=data,radius=rus,color=color,fill=True, fill_opacity=0.7).add_to(hmap)
       
       
hmap.save(path+'index.html')

f = open (path+'index.html','r', encoding="utf8")
indexhtml = f.read()
f.close()

statcounter = """  <!-- Default Statcounter code for Mapa Gasolinas
https://jlluch.github.io/ -->
<script type="text/javascript">
var sc_project=12749805; 
var sc_invisible=1; 
var sc_security="891e3230"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="real time web
analytics" href="https://statcounter.com/"
target="_blank"><img class="statcounter"
src="https://c.statcounter.com/12749805/0/891e3230/1/"
alt="real time web analytics"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code -->  """

index = indexhtml.find('</body>')
newindexhtml = indexhtml[:index]+statcounter+indexhtml[index:]
f = open (path+'index.html','w', encoding="utf8")
f.write(newindexhtml)
f.close()

