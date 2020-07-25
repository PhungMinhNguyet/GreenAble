import io
import requests
from io import BytesIO
import pandas as pd
from Rekognization import Rekognization 
class Classification:
    files = requests.get('https://docs.google.com/spreadsheets/d/1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI/export?format=csv&id=1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI&gid=0')
    assert files.status_code == 200, 'Wrong status code'
    data = files.content

    # import data to dataframe
    df = pd.read_csv(BytesIO(data), usecols=['Name','Type']) #unprocessed data
    # print few rows
    df.head()
    print(df)
    object=response["Labels"][0]["Name"]
    nrow,_ = df.shape
    #display circles represent for patients
    for i in range(0, nrow):
        name = df.iloc[i,0]
        if (str(name) == object):
            print(df['Type'][i])
        # else:
        #     print("Not given")