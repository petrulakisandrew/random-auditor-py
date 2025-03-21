import os
import pandas as pd 


REPORT_DIRECTORY = 'C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 1/DHA/2025/Raw Data/July 24.xlsx'
# test_data = {
#     'Name': ['Tenant1','Tenant2','Tenant3','Tenant4'],
#     'Caseworker': ['Caseworker1','Caseworker2','Caseworker3','Caseworker4'],
#     'City': ['City1','City2','City3','City4']
# }

df = pd.read_excel(REPORT_DIRECTORY)
df.fillna('N/A', inplace=True)

print(df)

# sampledtest_df = test_df.sample(n=3)
# print(sampledtest_df)