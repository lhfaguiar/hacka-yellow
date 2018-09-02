import googlemaps
import pandas as pd
import numpy as np
from numpy import nan
import re
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime

accident_frame = pd.read_csv('CET/MortosFeridos2011-2017/Mortos_e_Feridos_2011-2017_Ocorrencias_GeocodeFinalizado.csv', engine='python', error_bad_lines=False, delimiter=';')
perfil_frame = pd.read_csv('CET/MortosFeridos2011-2017/Mortos_e_Feridos_2011-2017_PerfilDasVitimas_ComLatLong.csv', engine='python', error_bad_lines=False, delimiter=';')

filtered_bike = accident_frame[accident_frame['bicicleta']!=0]
filtered_female = perfil_frame[perfil_frame['sexo']=='F']

female_bike = pd.merge(filtered_female, filtered_bike, how='inner', on=['id_acidente'])
female_bike = female_bike[np.isfinite(female_bike['latitude_y'])]
female_bike = female_bike[np.isfinite(female_bike['longitude_y'])]

female_bike.to_csv('acidentes_mulheres.csv')

labels = ['Homens', 'Mulheres']
sizes = [len(filtered_bike) - len(female_bike), len(female_bike)]
explode = [0, 0.1]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=['#AD1457', '#636363'])
ax1.axis('equal')
plt.tight_layout()
plt.savefig('AcidenteBikeHvsM.png')

caminho = ['TRES DE DEZEMBRO', 'QUINZE DE NOVEMBRO', 'JOAO MENDES', 'LIBERDADE', 'VERGUEIRO', 'PARAISO', 'BERNARDINO DE CAMPOS', 'PAULISTA']
acidentes_frame = pd.DataFrame(['rua', 'ocorrencias'])

coluna_end = female_bike['end_y']
# df.apply(lambda x: x['name'].count(x['SearchID']), axis=1)

coluna_end = str(coluna_end.str.cat(sep=' '))

# print coluna_end

for rua in caminho:
	print rua, coluna_end.count(rua)
	"""
	TRES DE DEZEMBRO 0
	QUINZE DE NOVEMBRO 1
	JOAO MENDES 0
	LIBERDADE 1
	VERGUEIRO 7
	PARAISO 0
	BERNARDINO DE CAMPOS 1
	PAULISTA 8
	"""


pos_ciclos = pd.to_datetime(female_bike['data'])
pos_ciclos = pos_ciclos.apply(lambda x: x.year)

pre_ciclos = pos_ciclos.value_counts(ascending = True)


print pre_ciclos
"""
2017     54
2016     59
2015     69
2014     87
2011     90
2013     96
2012    105
"""

pre = 105 + 96 + 87

pos = 69 + 59 + 54

print pre, pos


caminho2 = ['9 DE JULHO', 'BOA VISTA', 'LARGO DE SAO BENTO', 'LIBERO BADARO', 'MIGUEL COUTO', 'FORMOSA', 'NOVE DE JULHO', 'RUA ROCHA', 'ITAPEVA', 'PAMPLONA', 'PAULISTA']
for rua in caminho2:
	print rua, coluna_end.count(rua)



# rua tres de dezembro
# rua quinze de novembro
# praca da se
# praca doutor joao mendes
# avenida liberdade
# rua vergueiro
# rua do paraiso
# avenida bernardino campos
# avenida paulista


# datas_acidente = female_bike['data']
# anos_acidente = datas_acidente.datetime(YYYY)
# print anos_acidente


# fig1 = 

# fig1, ax1 = plt.subplots()
# ax1.graph()


# for index, row in female_bike:
# 	print row
# mapa = folium.Map([-23.5486, -46.6392], zoom_start=10, tiles="OpenStreetMap")

# print female_bike.dtypes

# for index, row in female_bike:	
# 	folium.Marker(float(row['latitude_y']), float(row['longitude_y'])).add_to(mapa)

# mapa.save('mapaacc.html')


# print female_bike

# AD1457
# FF80B




# logger = logging.getLogger("root")
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# logger.addHandler(ch)

