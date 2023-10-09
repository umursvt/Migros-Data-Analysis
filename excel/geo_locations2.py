import pandas as pd
import geocoder
def get_city_from_address(address):
    reversed_address = address[::-1]  # Adresi tersten oku
    index = reversed_address.find("/")  # "/" işaretinin konumunu bul

    if index != -1:
        city = str(reversed_address[:index][::-1]) # "/" işaretinden önceki kısmı tersten düzelt
        return city
    
    return None

def get_locations():
    excel_read = pd.read_excel('howden2.xlsx', sheet_name='Howden Consolidated Data')
    try:
        for index,row in excel_read.iterrows():
            codes=row['Enlem Boylam'] 
            if codes != 0 :    
                enlem, boylam = codes.split(',')
                location = geocoder.osm([enlem, boylam], method='reverse')
                if location.ok:
                    if 'province' in location.raw['address']:
                        town = location.raw['address']['province']
                        excel_read.at[index,'Şehir']=town                   
                        print(f"{town} kaydedildi. {row}")
                    else:
                        excel_read.at[index,'Şehir']='YOK'
                        if excel_read.at[index,'Şehir']=='YOK':
                            address = excel_read['Address']
                            excel_read["Şehir"] = address.apply(get_city_from_address)
                            print(f'Adresten çekildi.{row}')

                else:
                    excel_read.at[index,'Şehir']='YOK'
                    address = excel_read['Address']
                    excel_read["Şehir"] = address.apply(get_city_from_address)
                    print(f'Şehir veya kasaba bilgisi bulunamadı {row}')
            else:
                excel_read.at[index,'Şehir']='YOK'
                print('Sıfıra denk gelindi.')
    except KeyError as k :
        excel_read.at[index,'Şehir']='HATA'
        print(f'HATA {k}')
    
    excel_read.to_excel('deneme.xlsx', sheet_name='Howden Consolidated Data', index=False)

get_locations()
