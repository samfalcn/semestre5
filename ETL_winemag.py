import pandas as pd

#ETL

#EXTRACCIÓN
df = pd.read_csv("winemag-data-130k-v2.csv")

#TRANSFORMACIÓN
df_limpio = df.dropna()
df_null = df.isnull().sum()
variety = df.dropna(subset=['variety'])['variety']
country = df.dropna(subset=['country'])['country']
designation = df.dropna(subset=['designation'])['designation']
price = df.dropna(subset=['price'])['price']
province = df.dropna(subset=['province'])['province']
region_1 = df.dropna(subset=['region_1'])['region_1']
region_2 = df.dropna(subset=['region_2'])['region_2']
taster_name = df.dropna(subset=['taster_name'])['taster_name']

#CARGA
df_limpio.to_csv('df_limpio_vinos.csv')
variety.to_csv('df_variety.csv')
country.to_csv('df_country.csv')
designation.to_csv('df_designation.csv')
price.to_csv('df_price.csv')
province.to_csv('df_province.csv')
region_1.to_csv('df_region_1.csv')
region_2.to_csv('df_region_2.csv')
taster_name.to_csv('df_taster_name.csv')

#DATOS NULOS
nulos_country = df[df['country'].isnull()]
nulos_price = df[df['price'].isnull()]
nulos_desig = df[df['designation'].isnull()]
nulos_region1 = df[df['region_1'].isnull()]
nulos_region2 = df[df['region_2'].isnull()]
nulos_variety = df[df['variety'].isnull()]
nulos_points = df[df['points'].isnull()]

print(f'Cantidad de datos nulos en Country: {len(nulos_country)}')
print(f'Cantidad de datos nulos en Price: {len(nulos_price)}')
print(f'Cantidad de datos nulos en Points: {len(nulos_points)}')
print(f'Cantidad de datos nulos en Designation: {len(nulos_desig)}')
print(f'Cantidad de datos nulos en Region1: {len(nulos_region1)}')
print(f'Cantidad de datos nulos en Region2: {len(nulos_region2)}')
print(f'Cantidad de datos nulos en Variety: {len(nulos_variety)}')
