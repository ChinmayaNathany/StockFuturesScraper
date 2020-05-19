from bs4 import BeautifulSoup
import requests
import json
websites_list = []
from datetime import date
import csv

try:
    with open("data.json", "r") as fb:
        master_data = json.load(fb)
except:
    master_data = {}
    print("NEW DATABASE")

with open('websites.txt') as websites:
    for website in websites:
        websites_list.append(website.replace("\n", ''))
#print(websites_list)

for website in websites_list:
    html = requests.get(website)
    soup = BeautifulSoup(html.content, 'lxml')
    open_interest_data = soup.find('div', id='PriceFuturesTableBody').text
    open_interest_data = open_interest_data[open_interest_data.find('Open Interest'):]
    stock_name = soup.find('h1', class_='pcstname').text
    open_interest_data = open_interest_data.replace(",", '')
    open_interest_data = open_interest_data.split("\n")
    if stock_name not in master_data:
        master_data[stock_name] = {}

    price_data = soup.find('div', class_='pcnsb div_live_price_wrap').text
    price_data = price_data.replace(",", '')
    price_data = price_data.split("\n")
    ltp = float(price_data[1])
    price_change = float(price_data[3][:price_data[3].find(' ')])
    price_change_pct = float(price_data[3][price_data[3].find(' ') + 2: len(price_data[3]) - 2])
    # master_data[stock_name][date.today().strftime('%d/%m')] = {"LTP": ltp,
    #     "Price Change": price_change, "Price Change Percent": price_change_pct,
    #     "Open Interest": int(open_interest_data[1]), "Open Interest Change":
    #     int(open_interest_data[5]), "OI Change Percent": float(open_interest_data[9])}
    master_data[stock_name][date.today().strftime('%d/%m')] = [ltp, price_change, price_change_pct,
                                                               int(open_interest_data[1]), int(open_interest_data[5]),
                                                               float(open_interest_data[9])]



json_to_save = json.dumps(master_data)
with open("data.json", "w") as fb:
    fb.write(json_to_save)
