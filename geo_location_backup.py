import pandas as pd
import geocoder

def get_locations():
    excel_read = pd.read_excel('Data.xlsx', sheet_name='SHEET NAME')
    geo_codes = excel_read['Enlem Boylam']
    geo_codes.fillna('NEW YORK')
    enlemler = []
    boylamlar = []
    valid_data = []  # Geçerli verileri saklamak için boş bir liste
    
    for codes in geo_codes:
        enlem, boylam = codes.split(',')
        enlemler.append(enlem.strip())
        boylamlar.append(boylam.strip())
    
    en_boy = list(zip(enlemler, boylamlar))
    
    for i in en_boy:
        location = geocoder.osm([i[0], i[1]], method='reverse')
        
        if location.ok:
            if 'province' in location.raw['address']:
                town = location.raw['address']['province']
                new_row = {'Şehir': town}
                valid_data.append(new_row)
                print(f"{town} kaydedildi.")
            else:
                print('Şehir veya kasaba bilgisi bulunamadı')
        else:
            print('Bilgi bulunamadı')
    
    if valid_data:
        valid_df = pd.DataFrame(valid_data)
        excel_read = pd.concat([excel_read, valid_df], ignore_index=True)
        excel_read.to_excel('deneme.xlsx', sheet_name='SHEET NAME', index=False)

get_locations()
