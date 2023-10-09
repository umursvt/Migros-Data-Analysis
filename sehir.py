import pandas as pd

def get_city_from_address(address):
    reversed_address = address[::-1]  # Adresi tersten oku
    index = reversed_address.find("/")  # "/" işaretinin konumunu bul

    if index != -1:
        city = reversed_address[:index][::-1]  # "/" işaretinden önceki kısmı tersten düzelt
        return city
    
    return None

# Excel dosyasını oku
df = pd.read_excel("Data.xlsx", sheet_name="SHEET NAME")  

# Adresleri içeren sütunu oku
address = df['RİZİKO ADRESİ']

# Şehirleri bul
df["Şehir"] = address.apply(get_city_from_address)


df.to_excel("slash2.xlsx", sheet_name="SHEET NAME -- LAST", index=False)


