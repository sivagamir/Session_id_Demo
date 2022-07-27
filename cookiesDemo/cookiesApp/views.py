from django.shortcuts import render


# Create your views here.
def cookiesCountView(request):
    #count=request.COOKIES.get('count',0)
    count=request.session.get('count',0)
    totalCount=int(count) + 1
    request.session['count']=totalCount
    print(request.session.get_expiry_date())
    return render(request,"cookiesApp/cookiescount.html",{'count':totalCount})

    #response= render(request,"cookiesApp/cookiescount.html",{'count':totalCount})
    #response.set_cookie('count',totalCount)
    #return response
