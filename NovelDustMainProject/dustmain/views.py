from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import TopBooks,BookItems,Genre,Genrelist

# Create your views here.
def index(request):
    topbooks = TopBooks.objects.order_by('-date_added')
    contains = {'topbooks':topbooks}
    return render(request,'dustmain/index.html',context=contains)

def topbookpage(request,tbnameurl):
    tbname = tbnameurl.replace('-',' ')
    return render(request, 'dustmain/topbookpage.html')