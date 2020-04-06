from django.shortcuts import render , redirect,get_object_or_404
# from django.http import HttpResponse
# Create your views here.
from review.models import Product
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User

# from math import ceil

def index(request):
    products=Product.objects.all()
    paginator=Paginator(products,9)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    # n=len(products)
    # nslides=n//4 + ceil((n/4) -(n//4))
    # allprods=[]
    # catprods=Product.objects.values('catrgory')
    # cats={item['catrgory']for item in catprods}
    # for cat in cats:
        # prod=Product.objects.filter(catrgory=cat)
        # n=len(prod)
        # nslides=n//4 + ceil((n/4) -(n//4))
        # allprods.append([prod,range(1,nslides),nslides])
    # allprods=[[products,range(1,nslides),nslides],
    #           [products,range(1,nslides),nslides]]
    # params={'no_of_slides':nslides,'range':range(1,nslides+1),'products':products}
    # params={'allprods':allprods}
    params={'products':products}
    return render(request,'index.html',params)

def detail(request,pk):
    products=Product.objects.get(pk=pk)
    params={'products':products}
    return render(request,'test.html',params)


def about(request):
    return render(request,'review/about.html')

def contact(request):
    return render(request,'we are contact')

def tracker(request):
    return render(request,'we track order')

def search(request):
    return render(request,'we are search')

def prodView(request):
    return render(request,'we are prodView')

def checkout(request):
    return render(request,'we are checkout')

def handlesignup(request):
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         phone = request.POST['phone']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']

         myuser = User.objects.create_user(username ,email , pass1)
         myuser.Phone = phone
         myuser.save()
         messages.success(request,"your account successfully created")
         return redirect('/')
    else:
         return Httpresponse('Not allowed')

def handlelogin(request):
      if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        User =  authenticate(username =loginusername, password = loginpassword)
    
        if User is not None:
            login(request,User)
             
            return redirect('/') 
        else :
             messages.error(request,"Invalid Credentials")
             return redirect('/')
      return HttpResponse('handlelogin')

def handlelogout(request):
     logout(request)
     return redirect('/')


def like_post(request):
    product = get_object_or_404(Product,id=request.POST.get('prodt_id'))
    product.likes.add(request.User)
    return HttpResponseRedirect(post.get_absolute_url())


