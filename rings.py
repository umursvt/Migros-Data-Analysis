import pandas as pd
# excel MAĞAZA GROSS REVENUE
df_gross=pd.read_excel('Data.xlsx',sheet_name="SHEET NAME", dtype=({'Code':'Int64'}))


# Columns
storeCode =df_gross['COLUMN NAME']
totalPrice =df_gross['COLUMN NAME']


dictionary = dict(zip(storeCode,totalPrice))


# # Excel Sayfa1 page
dfsayfa = pd.read_excel('DATA2.xlsx',sheet_name='SHEET NAME2')








for i,j in dictionary.items():
    print('KEY: {}--- VALUE: {}'.format(i,j))


for i, j in dictionary.items():
    # finds the index
    row_index = dfsayfa.index[dfsayfa['COLUMN NAME']==i].tolist()
    print(row_index,i)
    
    if row_index:
        row_index = row_index[0]
        # fills the column's cells
        dfsayfa.at[row_index, 'COLUMN NAME '] = j 
        print(row_index,j)

# saves the file
dfsayfa.to_excel('DATA-last.xlsx',sheet_name='SHEET NAME -- LAST',index=False)

