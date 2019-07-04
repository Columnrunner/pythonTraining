# question: find the second last line from the string
import requests

Var = requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')

Rows = Var.text

Rows.split('\n')[-2]

#output
#run in terminal is 'python Mao.py'
#u'Emili,Cornner,ecornner3@sf_tuts.com,177 Magdeline Avenue,Norrk\xf6ping,8/13/2017'





# question: last second row 177 + 2
url = "https://todaybucket201917.s3.amazonaws.com/employees01.csv"

payload = "Hello World"
headers = {
    'Content-Type': "text/plain",
    'X-Amz-Content-Sha256': "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e",
    'Host': "todaybucket201917.s3.amazonaws.com",
    'X-Amz-Date': "20190703T185754Z",
    'Authorization': "AWS4-HMAC-SHA256 Credential=AKIA5UKXAZW6FBYZIFEX/20190703/us-east-1/s3/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date, Signature=7d625728d4c6bca6b14b3af18fbafd7375908030035f028a52d35a52ece5507c",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "eb9076ed-04f7-41dd-8750-6ee2ebb89f75,bbf5e1db-444c-43f8-a14c-e1d2d0622f7a",
    'accept-encoding': "gzip, deflate",
    'content-length': "11",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)    
list1 = response.text
lastSecondRow = list1.split('\n')[-2]
forthElement = lastSecondRow.split(',')[3]
oneSevenSeven = int(forthElement.split(' ')[0]) + 2


import datetime

print(datetime.datetime.strptime("01/27/2012","%m/%d/%Y"))