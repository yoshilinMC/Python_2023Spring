from twilio.rest import Client
from pathlib import Path
import pygsheets
import pandas as pd
import requests

# Set google cloud user Know the identity
gc = pygsheets.authorize(service_file="class7/rational-world-383208-b189dfd24b52.json")
# Google sheets know the sheet
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1sMgqvFoYYULSSEHTlABPPYUmtFCZ-pd24G7b7aQYRCU/edit#gid=0")
ws = sht[0]

"""
# read df
df = pd.DataFrame(ws.get_all_records())
print(df)
# clear
ws.clear()
# dataframe 
ws.set_dataframe(df, "A1") # Start at A1
"""
"""
gc = pygsheets.authorize(service_file="{ 金鑰 jason }")
sht = gc.open_by_url("{ google sheet }")
ws = sht.worksheet_by_title("工作表1")

d = {"Costumer Name":["小明","小華","小江", "Weight":[67, 44, 50]]}
df = pd.DataFrame(d)

ws.set_dataframe(df, "A1")
"""
"""
# 不帶條件
r = requests.get("{你想要要求的網站 url}")
# 有帶條件
payload = {"key1": "value1", "key2":"value2"}
# get
r = requests.get("{你想要要求的網站 url}", params=payload)
# post
r = requests.get("{你想要要求的網站 url}", data = {"keys":"value"})
"""
# r = requests.get("https://www.google.com/")
# print(r.status_code) # HTTP 狀態


url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("台幣對日幣的匯率為"+str(data["rates"]["JPY"]))