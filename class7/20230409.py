from twilio.rest import Client
from pathlib import Path
import pygsheets

"""
account_sid = 'ACe050c50fa69ce28a0ee188cde9c454f1'
auth_token = '6aabaa4d6444e16b17f0c59f0c19c30f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGdb02e85bb399eb619ee0e4f8fad9fb50',
    body='Test',
    to='+886910748511')

print(message.sid)
"""
"""
# 預設為指向開啟 Python (p = Path())
# 引入傳入指定位置
p = Path("class7/20230409.py")
# 找出絕對位置
print(p.resolve())
"""
# Set google cloud user Know the identity
gc = pygsheets.authorize(service_file="class7/rational-world-383208-b189dfd24b52.json")
# Google sheets know the sheet
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1sMgqvFoYYULSSEHTlABPPYUmtFCZ-pd24G7b7aQYRCU/edit#gid=0")
"""
# Choose the sheet
ws = sht[0]
# Use the name to choose the sheet
ws = sht.worksheet_by_title("工作表1")
ws.update_value("A1","Test")
# Read the sheet
value = ws.get_value("A1")
print("A1's value "+ value)
A1 = ws.cell("A1")
print("A1's value: "+ A1.value)
# Clear sheet
ws.clear()
"""
ws = sht[0]
ws.update_value("A1","Name")
ws.update_value("B1","Age")
ws.update_value("A2","Amy")
ws.update_value("B2","18")
ws.update_value("A3","Peter")
ws.update_value("B3","15")