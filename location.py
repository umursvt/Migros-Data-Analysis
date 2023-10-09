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


# Migros Dosyası
df_Migros = pd.read_excel('deneme.xlsx',sheet_name='Sayfa1')

# Migros Column Name
magazaNoMigros = df_Migros['Column Name']
print(magazaNoMigros)

#  Key=mağazaNo value=XKoordinat olmak üzere dict oluşturur.
magazaX = dict(zip(magazaNoListe,x))

#  Key=mağazaNo value=YKoordinat olmak üzere dict oluşturur.   
magazaY = dict(zip(magazaNoListe,y))

# Enlem
for i, j in magazaX.items():
    row_index = df_Migros.index[df_Migros['Column Name']==i].tolist()

    if row_index:
        row_index = row_index[0]
        df_Migros.at[row_index, 'Enlem'] = j

# Boylam
for i, j in magazaY.items():
    # satır index belirle
    row_index = df_Migros.index[df_Migros['Column Name']==i].tolist()
    if row_index:
        row_index = row_index[0]
        # satır sutun kesişimine veri gir
        df_Migros.at[row_index, 'Boylam'] = j

        


# dosya kaıyt
df_Migros.to_excel('deneme.xlsx',sheet_name='Sayfa1',index=False)
