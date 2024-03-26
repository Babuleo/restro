from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MyImageForm,customuserform

from .models import *
import random
from django.urls import reverse


from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    form = customuserform()  # Initialize the form outside of the if-else block

    if request.method == 'POST':
        form = customuserform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {'form': form, 'error': 'Registration successful'})
        # No need for else block here since the form instance is already updated

    return render(request, 'register.html', {'form': form})

def home(request):
    success_message = request.GET.get('success_message')
    allmenu=menus.objects.all()
    menus_=[]
    
    for i in allmenu:
        menus_.append(i)
    
    ran_item=random.sample(menus_,3)
    myform=MyImageForm()
    context={'form':myform,'allmenu':ran_item,'success_message': success_message}



    
    return render(request,"main/home.html",context)


def menu(request):

    allmenu=menus.objects.all()
    myform=MyImageForm()
    context={'form':myform,'allmenu':allmenu}

    


    return render(request,"main/menu.html",context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to dashboard or another URL
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    
    return render(request, 'login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def mycart(request):
    if request.user.is_authenticated:
        allcart=cart.objects.filter(user=request.user)
        myform=MyImageForm()
        

    
        
       
        total=0
    

        for i in allcart:

            print(i.item.price)
            total+=i.item.price

        context={'form':myform,'allcart':allcart,'total':total}
        return render(request,'main/mycart.html',context)

    
    
    return redirect('login')

def addcart(request,p_id):
    if request.method=='POST':
        if request.user.is_authenticated:
            if cart.objects.filter(user=request.user,item=p_id):
                return redirect('/',{'error':"allready added in the cart"})
            else:
                items=menus.objects.get(id=p_id)
                cart.objects.create(user=request.user,item=items)
                return redirect('/',{'success_message':"successfully added"})
        else:
            return redirect('login')
    return redirect('menu')


def menuaddcart(request,p_id):
    if request.method=='POST':
        if request.user.is_authenticated:
            if cart.objects.filter(user=request.user,item=p_id):
                return redirect('menu')
            else:
                items=menus.objects.get(id=p_id)
                cart.objects.create(user=request.user,item=items)
                return redirect('menu')
        else:
            return redirect('login')
    return redirect('menu')



def delete(request,id):
    if request.method=='POST':
    
        del_item=cart.objects.filter(user=request.user,item=id).first()
        print (del_item)
        if del_item:

            del_item.delete()
            
        
    return redirect('mycart')

def dia(request):
    
            
        
    return render(request,'inc/dia.html')


def orderform(request):
    if request.method=='POST':
        
        user=request.user
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        paymentstatus=request.POST['paymentMethod']
        
        itemss=cart.objects.filter(user=request.user)

        # print (itemss)
        total=0
        cartitem=[]

        for i in itemss:
            print (i.item.price)
            total+=i.item.price
            cartitem.append(i.item.dishname)
        ord_status='prosscing'

        order.objects.create(user=user,name=name,phone=phone,address=address,items=cartitem,total_price=total,order_status=ord_status,amount_status=paymentstatus)
        print(cartitem)

        success_message = "order successfully placed"
        return redirect(reverse('home') + f'?success_message={success_message}')

            

    
            
        
    return render(request,'main/orderform.html')

def myorder(request):
    if request.user.is_authenticated:
        orders=order.objects.filter(user=request.user)
        
        for i in orders:
            
            print(i.items)
            print(i.user)
            print(i.total_price)
            print(i.id)
        print(orders)
        
        # for i in all:
        #     disname=cart.objects.filter(=i)
            
            
        
        return render(request,'main/myorder.html',{'orders':orders}) 
    return render(request,'main/myorder.html') 
