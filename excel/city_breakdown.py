import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
from collections import Counter
import json

excel_read = pd.read_excel('data.xlsx')
excel_read2 = pd.read_excel('data.xlsx', sheet_name='SHEET NAME')

sehirler = excel_read['City'].unique()

city_counts = []
total_pd_bi_list=[]

for city in sehirler:
    total_pd = excel_read[excel_read['City'] == city]['TOTAL PD'].sum()
    total_bi = excel_read[excel_read['City'] == city]['TOTAL BI'].sum()
    eq_d = excel_read2[excel_read2['Şehir'] == city]['TOTAL EQ Deductible'].sum()
    city_count = len(excel_read[excel_read['City'] == city])
    total_pd_max = excel_read[excel_read['City'] == city]['TOTAL PD + BI'].max()
    total_pd_min = excel_read[excel_read['City'] == city]['TOTAL PD + BI'].min()
    total_pd_bi = total_pd + total_bi

    city_counts.append(city_count)  
    total_pd_bi_list.append(total_pd_bi)
    totalpd_bi=total_pd+total_bi
    new_row={
        'City':city,
        'No of Locations':city_count,
        'Min PDBI Value':total_pd_min,
        'Max PDBI Value':total_pd_max,
        'Total PDBI Value':total_pd_bi,
        'Total PD Value':total_pd,
        'Total BI Value':total_bi,
        'TOTAL EQ Deductible':eq_d
    }
    excel_read = pd.concat([excel_read, pd.DataFrame([new_row])], ignore_index=True)
    print('EKLENDİ')


chart_df = pd.DataFrame({
    'Cities':sehirler,
    'City Counts':city_counts
})
chart_df.sort_values(by='City Counts',ascending=False)
top_char_df = (chart_df.head(15))




trace = go.Bar(x=top_char_df['Cities'], y=top_char_df['City Counts'])

layout = go.Layout(
    title='City Counts',
    xaxis=dict(title='Cities'),
    yaxis=dict(title='City Count')
)
fig = go.Figure(data=[trace], layout=layout)
iplot(fig)

chart_df2 = pd.DataFrame({
    'Cities':sehirler,
    'Total PDBI':total_pd_bi_list
})
chart_df2.sort_values(by='Total PDBI',ascending=False)
top_chart_df2 = chart_df2.head(15)



trace_second =go.Bar(x=top_chart_df2['Cities'],y=top_chart_df2['Total PDBI'])
layout_second=go.Layout(
    title='Totol PD and BI Value by City',
    xaxis=dict(title='Cities'),
    yaxis=dict(title='Total PD + BI')
)
fig=go.Figure(data=[trace_second],layout=layout_second)
iplot(fig)



# excel_read.to_excel('statistic.xlsx', index=False)


# GeoJSON dosyasını yükleyin
with open('turkey.geojson', 'r', encoding='utf-8') as file:
    geojson_data = json.load(file)


data = pd.DataFrame({'City': sehirler, 'City Count': city_counts})

data.dropna(subset=['City'], inplace=True)
data.sort_values(by='City Count',ascending=False)
data_head=data.head(20)
fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson_data,
    featureidkey='properties.NAME_1',  
    locations=data_head['City'],
  
   
    colorscale='Reds', 
   
))

city_coordinates = {
    'ADANA': {'lat': 37.0000, 'lon': 35.3213},
    'ADIYAMAN': {'lat': 37.7648, 'lon': 38.2766},
    'AFYONKARAHİSAR': {'lat': 38.7500, 'lon': 30.5500},
    'AĞRI': {'lat': 39.7217, 'lon': 43.0567},
    'AKSARAY': {'lat': 38.3725, 'lon': 34.0259},
    'AMASYA': {'lat': 40.6499, 'lon': 35.8353},
    'ANKARA': {'lat': 39.9334, 'lon': 32.8597},
    'ANTALYA': {'lat': 36.8841, 'lon': 30.7056},
    'ARDAHAN': {'lat': 41.1104, 'lon': 42.7022},
    'ARTVİN': {'lat': 41.1839, 'lon': 41.8183},
    'AYDIN': {'lat': 37.8444, 'lon': 27.8458},
    'BALIKESİR': {'lat': 39.6484, 'lon': 27.8826},
    'BARTIN': {'lat': 41.5811, 'lon': 32.4611},
    'BATMAN': {'lat': 37.8812, 'lon': 41.1351},
    'BAYBURT': {'lat': 40.2558, 'lon': 40.2249},
    'BİLECİK': {'lat': 40.1506, 'lon': 30.4172},
    'BİNGÖL': {'lat': 38.8854, 'lon': 40.4988},
    'BİTLİS': {'lat': 38.4041, 'lon': 42.1167},
    'BOLU': {'lat': 40.7392, 'lon': 31.6113},
    'BURDUR': {'lat': 37.7209, 'lon': 30.2907},
    'BURSA': {'lat': 40.1826, 'lon': 29.0669},
    'ÇANAKKALE': {'lat': 40.1553, 'lon': 26.4142},
    'ÇANKIRI': {'lat': 40.6013, 'lon': 33.6134},
    'ÇORUM': {'lat': 40.5506, 'lon': 34.9556},
    'DENİZLİ': {'lat': 37.7765, 'lon': 29.0864},
    'DİYARBAKIR': {'lat': 37.9204, 'lon': 40.2306},
    'DÜZCE': {'lat': 40.8438, 'lon': 31.1648},
    'EDİRNE': {'lat': 41.6818, 'lon': 26.5700},
    'ELAZIĞ': {'lat': 38.6740, 'lon': 39.2238},
    'ERZİNCAN': {'lat': 39.7500, 'lon': 39.5000},
    'ERZURUM': {'lat': 39.9208, 'lon': 41.2759},
    'ESKİŞEHİR': {'lat': 39.7767, 'lon': 30.5206},
    'GAZİANTEP': {'lat': 37.0662, 'lon': 37.3833},
    'GİRESUN': {'lat': 40.9128, 'lon': 38.3895},
    'GÜMÜŞHANE': {'lat': 40.4600, 'lon': 39.4822},
    'HAKKARİ': {'lat': 37.5736, 'lon': 43.7400},
    'HATAY': {'lat': 36.2154, 'lon': 36.1628},
    'IĞDIR': {'lat': 39.9167, 'lon': 44.0450},
    'ISPARTA': {'lat': 37.7666, 'lon': 30.5667},
    'İSTANBUL': {'lat': 41.0082, 'lon': 28.9784},
    'İZMİR': {'lat': 38.419200, 'lon': 27.128700},
    'KAHRAMANMARAŞ': {'lat': 37.5717, 'lon': 36.9372},
    'KARABÜK': {'lat': 41.2061, 'lon': 32.6200},
    'KARAMAN': {'lat': 37.1811, 'lon': 33.2150},
    'KARS': {'lat': 40.5956, 'lon': 43.0772},
    'KASTAMONU': {'lat': 41.3875, 'lon': 33.7831},
    'KAYSERİ': {'lat': 38.7333, 'lon': 35.4833},
    'KIRIKKALE': {'lat': 39.8468, 'lon': 33.5153},
    'KIRKLARELİ': {'lat': 41.7333, 'lon': 27.2167},
    'KIRŞEHİR': {'lat': 39.1458, 'lon': 34.1600},
    'KİLİS': {'lat': 36.7184, 'lon': 37.1211},
    'KOCAELİ': {'lat': 40.8533, 'lon': 29.8815},
    'KONYA': {'lat': 37.8651, 'lon': 32.4821},
    'KÜTAHYA': {'lat': 39.4167, 'lon': 29.9833},
    'MALATYA': {'lat': 38.3552, 'lon': 38.3095},
    'MANİSA': {'lat': 38.6191, 'lon': 27.4289},
    'MARDİN': {'lat': 37.3212, 'lon': 40.7249},
    'MERSİN': {'lat': 36.8000, 'lon': 34.6333},
    'MUĞLA': {'lat': 37.2153, 'lon': 28.3636},
    'MUŞ': {'lat': 38.7448, 'lon': 41.5065},
    'NEVŞEHİR': {'lat': 38.6936, 'lon': 34.6850},
    'NİĞDE': {'lat': 37.9667, 'lon': 34.6833},
    'ORDU': {'lat': 40.9839, 'lon': 37.8769},
    'OSMANİYE': {'lat': 37.2519, 'lon': 36.2731},
    'RİZE': {'lat': 41.0201, 'lon': 40.5234},
    'SAKARYA': {'lat': 40.7831, 'lon': 30.4017},
    'SAMSUN': {'lat': 41.2867, 'lon': 36.3300},
    'SİİRT': {'lat': 37.9333, 'lon': 41.9500},
    'SİNOP': {'lat': 42.0211, 'lon': 35.1531},
    'SİVAS': {'lat': 39.7483, 'lon': 37.0161},
    'ŞANLIURFA': {'lat': 37.1671, 'lon': 38.7939},
    'ŞIRNAK': {'lat': 37.5164, 'lon': 42.4610},
    'TEKİRDAĞ': {'lat': 40.9833, 'lon': 27.5167},
    'TOKAT': {'lat': 40.3081, 'lon': 36.5550},
    'TRABZON': {'lat': 41.0053, 'lon': 39.7264},
    'TUNCELİ': {'lat': 39.1086, 'lon': 39.5475},
    'UŞAK': {'lat': 38.6742, 'lon': 29.4056},
    'VAN': {'lat': 38.4942, 'lon': 43.3836},
    'YALOVA': {'lat': 40.6500, 'lon': 29.2667},
    'YOZGAT': {'lat': 39.8171, 'lon': 34.8147},
    'ZONGULDAK': {'lat': 41.2500, 'lon': 31.8333},
}



for i in range(len(data_head['City'])):
    city = data_head['City'][i]
    city_count = data_head['City Count'][i]
    marker_size = city_count * 0.1
    opacity = 1 

    if city in city_coordinates:
        lat = city_coordinates[city]['lat']
        lon = city_coordinates[city]['lon']
 
    hover_text = f"City: {city}<br>City Count: {city_count}"

    fig.add_trace(go.Scattermapbox(
        lat=[lat],  
        lon=[lon],  
        mode='markers',
        marker=dict(size=marker_size, sizemode='diameter', opacity=opacity, color='red'),
        hoverinfo='lon+lat+text',
        text=hover_text,
        name=f"{city} {city_count}"
    ))

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={'lat': 39.9334, 'lon': 32.8597},
    title='City Counts in Turkey with Density Points',
)


iplot(fig)


