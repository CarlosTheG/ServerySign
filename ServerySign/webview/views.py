from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import models
from django.template import Context, loader

def simplePrint(request):
    """
    A very simple page that just renders to test url routing
    """
    foodList = models.getServeryData()
    foodString = "<br />".join(foodList)
    return HttpResponse(foodString)

def index(request):
    """
    """
    foodList = models.getServeryData()
    foodString = "<br />".join(foodList)
    t = loader.get_template("app/index.html")
    c = {'foodList': foodList,'foodString':foodString}
    return render(request, "app/index.html", c)
    #return HttpResponse(t.render(c))