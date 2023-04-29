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

url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
usd = data["rates"]["USD"]
jpy = data["rates"]["JPY"]
hkd = data["rates"]["HKD"]
ws.update_value("A1","country")
ws.update_value("A2","America")
ws.update_value("A3","Japan")
ws.update_value("A4","Hong Kong")
ws.update_value("B1","匯率(以台做基準)")
ws.update_value("B2",usd)
ws.update_value("B3",jpy)
ws.update_value("B4",hkd)