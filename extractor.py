from apscheduler.schedulers.background import BlockingScheduler
from bs4 import BeautifulSoup as bs
import requests 
import json 

scheduler = BlockingScheduler() 

def extractor():
	html = bs(requests.get('http://www.cngnow.com/average-cng-prices/pages/default.aspx').content, 'html.parser')  
	prices = [price.string for price in html.find_all('div', class_='statePrice')]
	states = [state.string for state in html.find_all('div', class_='stateName')]
	results = [{'state': state, 'price': price} for state, price in zip(states, prices)]
	return json.dumps(results)
	
def update(): 
	f = open('data', 'w+')
	results = extractor() 
	f.write(results)
	f.close() 
	return 
	
def main(): 
	update()
	scheduler.add_job(update, 'cron', hour=17) 
	scheduler.start() 
	
	
if __name__ == "__main__": 
	main() 
