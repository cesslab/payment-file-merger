import pandas as pd
import os
import datetime

num_subjects = 14

path = os.path.dirname(os.path.abspath(__file__))
print(path)
df_ztree = pd.read_csv(os.path.join(path, 'files', 'ztree.pay'), sep='\t', skiprows=[num_subjects + 1])

df_otree = pd.read_excel(os.path.join(path,'files', 'otree.xlsx'), usecols=['Label', 'Total'])
df_otree['Label'] = df_otree['Label'].str.lower()

df_ztree['Profit'] = df_otree['Total'] + df_ztree['Profit']
df_ztree['Profit'] = df_ztree['Profit'].round(decimals=2)

file_name = 'payment_{}.pay'.format(datetime.datetime.now().isoformat())
df_ztree.to_csv(os.path.join(path, 'out', file_name), index=False, sep='\t')
