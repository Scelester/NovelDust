from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import TopBooks,BookItems,Genrelist
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time



# Create your views here.
def index(request):
    topbooks = TopBooks.objects.order_by('-date_added')
    
    #  for pagination

    page = request.GET.get('page',1)
    paginator = Paginator(topbooks,20)

    try:
        topbooks = paginator.page(page)
    except PageNotAnInteger:
        topbooks = paginator.page(1)
    except EmptyPage:
        topbooks = paginator.page(paginator.num_pages)

    # for search bar
    search_query = request.GET.get('search')
    if search_query:
        topbooks = TopBooks.objects.filter(topname__icontains=search_query)



    # final data send
    contains = {'topbooks':topbooks}
    return render(request,'noveldust/index.html',context=contains)






def topbookpage(request,tbnameurl):
    tbname = tbnameurl.replace('-',' ')
    tb = TopBooks.objects.get(topname=tbname)
    bkitem = tb.bookitems_set.order_by('volume_no')
    try:
        upb = bkitem[0]
        updated = upb.date_updated
    except:
        updated = 'never'

    content = {'tb':tb,'bkitem':bkitem,'updated':updated}
    return render(request, 'noveldust/topbookpage.html',content)




def searchview(request):
    search_query = request.GET.get('search')
    topbooks = TopBooks.objects.filter(topname__icontains=search_query)[:30]
    contains = {'topbooks':topbooks,'sqr':search_query}
    return render(request,'noveldust/index.html',context=contains)