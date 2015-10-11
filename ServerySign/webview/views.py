from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib2
#from app.models import ServeryMenu

# Create your views here.

def simplePrint(request):
    """
    A very simple page that just renders to test url routing
    """
    foodList = getServeryData()
    foodString = "<br />".join(foodList)
    return HttpResponse(foodString)

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
