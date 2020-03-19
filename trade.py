#!/usr/bin/python3

import requests
import alpaca_trade_api as tradeapi

BASEURL = 'https://paper-api.alpaca.markets'
ACCURL = '{}/v2/account'.format(BASEURL)
POSURL = '{}/v2/positions'.format(BASEURL)

UNKNOWN = 'api.alpaca.markets/paper-api.alpaca.markets'

APIKEY = "PK61TNWINAVOEE9C610J"
SECRETKEY = "oqsxqFZWaIEj7Tu3ev4o8kCcttieV6kuvbV4CAtk"

################# Style 1 ############################'

#print ( "----------------- Using nice .REST Helper Entity class methods ------------------ ")
#print ( f"**debug** - Base URL: {BASEURL}")
#print ( f"**debug** - Account URL: {ACCURL}")
#print ( f"**debug** - Positions URL: {POSURL}")

rx = tradeapi.REST('PK61TNWINAVOEE9C610J', 'oqsxqFZWaIEj7Tu3ev4o8kCcttieV6kuvbV4CAtk', 'https://paper-api.alpaca.markets', 'v2' )
acct_info = rx.get_account()
pos_info = rx.list_positions()

#print ( f"---------------- Account info ------------------" )
#print ( acct_info )

#print ( f"---------------- Positions info ------------------" )
#for i in range(len(pos_info)):
#    print ( f"Item #{i} \n {pos_info[i]}" )

print ( " " )
print ( f"---------------- Stock price info ------------------" )
print ( " " )
print ( f"RAW format data..." )
print ( f"--------------------" )

price_info = rx.get_barset(symbols='CODX', timeframe='1Min', limit=15)
stock_bars = price_info['CODX']
print ( f"Look inside ALL the data we extracted:\n {price_info}" )
print ( " " )
print ( f"Look at Price info for CODX:\n {stock_bars}" )

#for k, v in price_info.items():
#    print ( f"**KEY: {k}" )

print ( " " )
print ( f"Pretty &  nice formatted data..." )
print ( f"---------------------------------" )
my_keys = price_info.keys()
list_of_my_keys = list(my_keys)

print ( f"**LIst of all DICT keys: {list_of_my_keys}" )
print ( f"**Key 0 is: {list_of_my_keys[0]}" )
#print ( price_info[list_of_my_keys[0]] )
data_list = price_info[list_of_my_keys[0]]
for i in range(len(data_list)):
    print ( f"DATA ITEM #{i} is -> {data_list[i]}" )

# Now access very specific parts of the data strcuitures
num_of_datapoints = len(data_list)
first_open = stock_bars[0].o
last_close = stock_bars[-1].c
percent_change = round( ((last_close - first_open) / first_open * 100),4 )
print ( " " )
print ( f"Access specific data fields from the complex data structure..." )
print ( f"---------------------------------------------------------------" )
print ( f"FIRST OPEN price: {first_open}" )
print ( f"LAST CLOSE price: {last_close}" )
print ( "CODX moved {}% in the last {} data points.".format(percent_change, num_of_datapoints))

################# Style 2 ############################'

# print ( " " )
# print ( "------------- Testing RAW Request method ---------------" )
# r = requests.get( ACCURL, headers={'APCA-API-KEY-ID': APIKEY, 'APCA-API-SECRET-KEY': SECRETKEY} )

#print (r.content)
