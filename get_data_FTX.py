import requests
import pandas as pd
import matplotlib.pyplot as plt

#Get all futures data using FTX api
def get_futures_data():
	futures_markets = requests.get('https://ftx.com/api/futures').json()
	futures_market_df = pd.DataFrame(futures_markets['result'])
	return futures_market_df

#Filter the df with all the future data to extract move contracts
def filter_move_contract(df):
	move_futures =df[df.name.str.contains('MOVE')]
	return move_futures

#Get only the relevant data : prices and expiration
def sort_data(df):
	sorted_data = df.filter(['expiry', 'last'])
	sorted_data['expiry'] = pd.to_datetime(sorted_data['expiry'])
	return sorted_data

def plot_term_structure(data):
	data.plot()
	plt.show()
	
futures_request = get_futures_data()
move_contracts = filter_move_contract(futures_request)
move_filtered = sort_data(move_contracts)
plot_term_structure(move_filtered)