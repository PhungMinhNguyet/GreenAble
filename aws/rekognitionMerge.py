import csv
import boto3
access_key_id = "AKIASQUY6JJGAWRLTIOO"
secret_access_key = "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"
region = "ap-southeast-1"
# with open ('credential.csv','r') as input:
#     next(input)
#     reader=csv.reader(input)
#     input.close()
# for line in reader:
#     print(line)
#     access_key_id= line[3]
#     secret_access_key= line[4]
photo= 'chai.jpg' 
client= boto3.client('rekognition',region_name="ap-southeast-1",
# region=region,
 aws_access_key_id= access_key_id,
 aws_secret_access_key= secret_access_key)  
with open(photo,'rb')as source_image:
    source_bytes= source_image.read()  
response= client.detect_labels(Image={'Bytes':source_bytes},
MaxLabels=10,
MinConfidence=95)
# print(response["Labels"]) 
print(response["Labels"][0]["Confidence"], "%")  
import io
import requests
from io import BytesIO
import pandas as pd
files = requests.get('https://docs.google.com/spreadsheets/d/1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI/export?format=csv&id=1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI&gid=0')
assert files.status_code == 200, 'Wrong status code'
data = files.content

# import data to dataframe
df = pd.read_csv(BytesIO(data), usecols=['Name','Type']) #unprocessed data
# print few rows
df.head()
# print(df)
object=response["Labels"][0]["Name"]
nrow,_ = df.shape
#display circles represent for patients
for i in range(0, nrow):
    name = df.iloc[i,0]
    if (str(name) == object):
        print(df['Type'][i])
    # else:
    #     print("Not given")