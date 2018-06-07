from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time

app=Flask(__name__)

@app.route('/')
def index():
	res= requests.get("https://www.hbo.com/series/all-series")
	soup= BeautifulSoup(res.text,'html.parser')
	ser= soup.findAll('p',{'class':'modules/cards/CatalogCard--title'})

	series=[]

	for x in ser:
		series.append(x.text)
	
	
	return render_template("index.html", series=series)
    
#driver= webdriver.Firefox()
#time.sleep(5)

if __name__=='__main__':
	print("hello")
	app.jinja_env.globals.update(chr=chr)
	print("Hi")
	app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
	
	#driver.get('localhost:8000')

