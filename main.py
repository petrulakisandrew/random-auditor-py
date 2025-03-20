import os
import pandas as pd 

test_data = {
    'Name': ['Tenant1','Tenant2','Tenant3','Tenant4'],
    'Caseworker': ['Caseworker1','Caseworker2','Caseworker3','Caseworker4'],
    'City': ['City1','City2','City3','City4']
}

# print(test_data)

test_df = pd.DataFrame(test_data, columns = ['Name','Caseworker','City'])

# print(test_df)

sampledtest_df = test_df.sample(n=3)
print(sampledtest_df)