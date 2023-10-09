import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
import seaborn as sns
sns.set()

excel_read = pd.read_excel('howden_2last.xlsx',sheet_name='EQ ZONE')


eq_zones = excel_read['TR EQ ZONES'].unique()




for zone in eq_zones:
    total_pd = excel_read[excel_read['TR EQ ZONES']==zone]['PROPERTY(USD)'].sum()
    total_bi = excel_read[excel_read['TR EQ ZONES']==zone]['BI(USD)'].sum()
    total_pd_bi = total_pd + total_bi
    totalpd_bi=total_pd+total_bi
    new_row={
        'TR EQ ZONES':zone,
        'PROPERTY(USD)':total_pd,
        'BI(USD)':total_bi,
        'TOTAL SUM(USD)':total_pd_bi,
       
    }
    excel_read = pd.concat([excel_read, pd.DataFrame([new_row])], ignore_index=True)

total_sum_column = excel_read['TOTAL SUM(USD)'].head(7)
per_ = (total_sum_column/totalpd_bi)*100





print('Chart is preparing..')

trace = go.Pie(
    labels=eq_zones,
    values=per_,
    textinfo='percent+label',
    hoverinfo='label+percent',
    hole=0.7  
)

layout = go.Layout(title='Donut Chart of EQ Zones')


fig = go.Figure(data=[trace], layout=layout)


iplot(fig)

excel_read.to_excel('statistic2.xlsx', index=False)





