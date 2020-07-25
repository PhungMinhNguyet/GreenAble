import io
import requests
from io import BytesIO
import pandas as pd
response = requests.get('https://docs.google.com/spreadsheets/d/1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI/export?format=csv&id=1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI&gid=0')
assert response.status_code == 200, 'Wrong status code'
data = response.content

# import data to dataframe
df = pd.read_csv(BytesIO(data), usecols=['Name','Type']) #unprocessed data
# print few rows
df.head()
print(df)
object="Bottle"
nrow,_ = df.shape
#display circles represent for patients
for i in range(0, nrow):
    name = df.iloc[i,0]
    if (str(name) == object):
        print(df['Type'][i])
    else:
        print("Not given")