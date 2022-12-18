import pandas as pd
import numpy 
import matplotlib as plt 

df = pd.read_csv("IMDb_All_Genres_etf_clean1.csv")

# genres = df['main_genre'].drop_duplicates()
# genres_list = genres.tolist()

director = df['Director'].drop_duplicates()
director_list = director.tolist()
new_list = []
for i in director_list:
    new_list.append(i.replace('Directors:', '').split(','))
flat= []
for item in new_list:
    flat+= item

z = 0
y = 0
dict = {}
a = len(flat)
while (z < a):
    Movies = []
    director = str(flat[z])
    for value in range(len(df)):
        if director in str(df['Director'].iloc[value]):
            Movies.append(df['Movie_Title'].iloc[value])
        y = y + 1
        count = len(list(Movies))
    dict[z] = {'Director' : director, 'Movies' : Movies, 'Counter' : count}
    z = z + 1

b= []
c = []
for x in range(10):
    b.append(dict[x]['Director'])
    c.append(dict[x]['Counter'])

plt.plot(b, c)
plt.show()
print('a')