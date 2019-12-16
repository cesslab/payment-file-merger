import pandas as pd
import os
import time

num_subjects = 14

path = os.path.dirname(os.path.abspath(__file__))

df_ztree = pd.read_csv(os.path.join(path, 'in', 'ztree.pay'), sep='\t', skiprows=[num_subjects + 1])
df_otree = pd.read_excel(os.path.join(path, 'in', 'otree.xlsx'), usecols=['Label', 'Total'])

payoffs = df_otree.merge(df_ztree, left_on='Label', right_on='Computer')
payoffs['Final_Profit'] = payoffs['Total'] + payoffs['Profit']
print(payoffs)

df_ztree['Profit'] = payoffs['Final_Profit'].round(decimals=2)
df_ztree.sort_values(by=['Computer'], inplace=True)

file_name = 'payment_{}.pay'.format(time.strftime('%Y%m%d_%H%M%S'))
df_ztree.to_csv(os.path.join(path, 'out', file_name), index=False, sep='\t')
