from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.

def simplePrint(request):
    """
    A very simple page that just renders to test url routing
    """
    foodList = models.getServeryData()
    foodString = "<br />".join(foodList)
    return HttpResponse(foodString)
