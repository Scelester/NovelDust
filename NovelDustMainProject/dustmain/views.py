from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import BookItemsForm,Topbookform

# Create your views here.
def index(request):
    
    if request.method != 'POST':
        topform = Topbookform()
    else:
        topform = Topbookform(data=request.POST)
        if topform.is_valid():
            topform.save()
    
    return render(request,'dustmain/index.html',)
    
