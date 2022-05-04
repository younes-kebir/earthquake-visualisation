import pandas as pd



'''
Dans cett premiere partie, on va preparer les données à traiter ! 
le fichier "seisme_world_07_12_2021.csv" contient les données des seismes de la deuxieme moitié de l'année 2021
On va s'interesser aux colonnes :time, latitude, longitude, place, mag et depth
'''

df = pd.read_csv('seisme_world_07_12_2021.csv', usecols = ['time', 'latitude', 'longitude', 'place', 'mag', 'depth'])

'''
On renome les colonnes 
time : instant
latitude : lat
longitude : lon
depth : profondeur 
place : pays
'''

df = df.rename(columns={'time':'instant','latitude':'lat','longitude':'lon','depth':'profondeur','place':'pays'})

'''
On convertit la colonne "instant" à la forme datetime de Pandas
 '''
df['instant'] = pd.to_datetime(df['instant'])


df.dropna(inplace=True) # On supprimes les lignes qui contiennent des données nul 

'''
Pour les endroits, on utilise la fonction "str.rsplit" pour décomposer les données, 
on ne prendra que le pays ou l'etat pour les états-unis
'''
pays_split = df['pays'].str.rsplit(",", n = 1, expand = True)

'''
pays_split contient deux colonnes, on ajoute la colonne "endroit" qui contient le pays/etat des seismes
'''
df['endroit'] = pays_split[1]

'''
On supprime la colonne "pays"
'''
df.drop(columns = ['pays'], inplace = True)

'''
Pour l'esthétique, on va reindexer les colonnes comme suit
'''
df = df.reindex(columns=['instant','lat','lon','endroit','mag','profondeur'])

'''
On exporte les données en un fichier csv
'''
df.to_csv('seisme_2021.csv', index='false')