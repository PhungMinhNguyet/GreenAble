import csv
import boto3
class Rekognition:
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
    return response["Labels"][0]["Name"]
    # print(response["Labels"]) 
    # print(response["Labels"][0]["Name"])  
