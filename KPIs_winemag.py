import pandas as pd
import statistics
import numpy 
import matplotlib.pyplot as plt

df = pd.read_csv("winemag-data-130k-v2.csv")

country_null = df['country'].fillna('null').tolist()
price = df.dropna(subset=['price'])['price'].tolist()

def price_stats():
    a = len(price)
    c = sum(price)
    d = statistics.pstdev(price)
    m = max(price)
    mi = min(price)
    print(f'Media del precio: ${(c/a)}')
    print(f'Desviación estandar del precio: ${d}')
    print(f'Precio más alto: ${m}')
    print(f'Precio más bajo: ${mi}')

def per_country():
    print('Cantidad de vinos evaluados por país:')
    c = dict()
    g = []
    u = []
    for n in country_null:
        if n in c.keys():
            c[n] = c[n] + 1
        else: 
            c[n] = 1
    for z in c:
        print(z, ':', (c[z]))
        g.append(c[z])
        u.append(z)
        # print(z, ':', str(c[z]))
     
    plt.bar(u, g)
    plt.ylabel('vinos evaluados')
    plt.xticks(rotation = 90)
    plt.grid()
    plt.show()


def max_min():
    c = dict()
    for n in country_null:
        if n in c.keys():
            c[n] = c[n] + 1
        else: 
            c[n] = 1
    h = max(c, key=c.get)
    y = [key for key, value in c.items() if value == min(c.values())]
    print(f'País con mayor cantidad de vinos evaluados: {h}')
    print(f'Países con menor cantidad de vinos evaluados: {y}')

def quality_price():
    price_df = df.dropna(subset=['price'])
    winery = price_df['winery'].tolist()
    points = price_df['points'].tolist()
    price = price_df['price'].tolist()
    country = price_df['country'].tolist()
    z = 0
    dic = {}
    for i in range(len(price_df)):
        dic[i] = {
        'country' : country[i],
        'winery' : winery[i], 'price': price[i], 
        'points' : points[i], 'qp_indicator' : (points[i]/price[i])
     }   
    indicator = 0
    for j in range(len(dic)):
        while dic[j]['qp_indicator'] > indicator:
            indicator = dic[j]['qp_indicator']
            h = j
    print('Indicador más alto de calidad-precio:')
    print(dic[h])

    b= []
    c = []
    for x in range(30):
        b.append(dic[x]['winery'])
        c.append(dic[x]['qp_indicator'])
    plt.bar(b, c)
    plt.ylabel('índice de calidad-precio')
    plt.xticks(rotation = 90)
    plt.grid()
    plt.show()

def points_country():
    price_df = df.dropna(subset=['points'])
    df1 = price_df.dropna(subset=['country'])
    country = price_df['country'].drop_duplicates().tolist()
    z = 0
    dict = {}
    a = len(country)
    while (z < a):
        puntos = []
        d = str(country[z])
        for value in range(len(df1)):
            if d in str(df1['country'].iloc[value]):
                puntos.append(df1['points'].iloc[value])
                count = len(list(puntos))
        dict[z] = {'País' : d, 'Promedio' : sum(puntos)/count}
        z = z + 1
    indicator = 0
    for j in range(len(dict)):
        while dict[j]['Promedio'] > indicator:
            indicator = dict[j]['Promedio']
            h = j
    print('País con el promedio más alto de puntos:')
    print(dict[h])



# per_country()
# max_min()
# price_stats()
# quality_price()
points_country() 