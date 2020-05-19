# Python program to convert 
# JSON file to CSV 


import json
import csv

# Opening JSON file and loading the data 
# into the variable data 
with open('data.json') as json_file:
    data = json.load(json_file)

stocks_data = data

# now we will open a file for writing 
data_file = open('data_file0.csv', 'w')

# create the csv writer object 
csv_writer = csv.writer(data_file)

# Counter variable used for writing  
# headers to the CSV file 
count = 0

for stock in stocks_data.keys():
    if count == 0:
        # Writing headers of CSV file
        print(stocks_data[stock])
        header = list(stocks_data[stock].keys())
        num_dates = len(header)
        head = ['Stock Name']
        for date in stocks_data[stock].keys():
            head.extend([str(date), '', '', '', '', ''])
        csv_writer.writerow(head)
        count += 1
        headd2 = [" "]
        head2 = ["LTP", "Price Chg", "Price Chg %", "OI", "OI Chg", "OI Chg %"] * num_dates
        headd2.extend(head2)
        csv_writer.writerow(headd2)

    stock_data = [stock]
    for date in stocks_data[stock].keys():
        stock_data.extend(stocks_data[stock][date])
    csv_writer.writerow(stock_data)


    # # Writing data of CSV file
    # csv_writer.writerow(stock_data[stock].values())

data_file.close() 