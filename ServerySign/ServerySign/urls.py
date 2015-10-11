
"""ServerySign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import urllib2
#from webview.views import simplePrint

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
    			foodList.append(item.get_text())
    foodList.pop(-1)
    return foodList 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'webview/$', simplePrint),
]

