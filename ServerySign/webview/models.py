from django.db import models
from bs4 import BeautifulSoup
import urllib2

def getServeryData():
    response = urllib2.urlopen('http://dining.rice.edu')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    foodList = []
    for servery in soup.findAll("div", class_="servery-title"):
    	if (servery.get_text() == "\nWest\n"):
    		unorderedList = servery.next_sibling.next_sibling
    		for item in unorderedList.findAll('li'):
    			foodList.append(item.get_text().title())
    foodList.pop(-1)
    return foodList 
