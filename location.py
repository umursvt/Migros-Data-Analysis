import pandas as pd
# Liste dosyasını okur
df_Liste = pd.read_excel('Data.xlsx')
# Column Name kolonunu okur
magazaNoListe=df_Liste['Column Name']
print(magazaNoListe)
# X Koordinat kolonunu okur
x=df_Liste['X Koordinat']
# Y Koordinat kolonunu okuK
y = df_Liste['Y Koordinat']


# read excel data
df_Migros = pd.read_excel('deneme.xlsx',sheet_name='Sayfa1')

# Get Column Name
magazaNoMigros = df_Migros['Column Name']
print(magazaNoMigros)

# create Dict Key=mağazaNo value=XKoordinat 
magazaX = dict(zip(magazaNoListe,x))

#  create Dict Key=mağazaNo value=YKoordinat 
magazaY = dict(zip(magazaNoListe,y))

# Latitude
for i, j in magazaX.items():
    row_index = df_Migros.index[df_Migros['Column Name']==i].tolist()

    if row_index:
        row_index = row_index[0]
        df_Migros.at[row_index, 'Enlem'] = j

# longitude
for i, j in magazaY.items():
    # indexing
    row_index = df_Migros.index[df_Migros['Column Name']==i].tolist()
    if row_index:
        row_index = row_index[0]
        df_Migros.at[row_index, 'Boylam'] = j

        


# save the last excel
df_Migros.to_excel('result.xlsx',sheet_name='Sayfa1',index=False)
