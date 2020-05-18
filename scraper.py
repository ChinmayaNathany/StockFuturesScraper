from bs4 import BeautifulSoup
import requests
master_data = {}
websites_list = []

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

    master_data[stock_name] = {"Open Interest": int(open_interest_data[1]), "Open Interest Change":
        int(open_interest_data[5]), "Change Percent": float(open_interest_data[9])}

print(master_data)


