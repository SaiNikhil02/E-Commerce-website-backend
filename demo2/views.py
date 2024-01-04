
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import RegisterForm,ProductForm
from .models import Product, Category,Cart
from django.contrib.auth.decorators import login_required

def custom_login(request): 
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password'] 
        user=authenticate(request, username=username,password=password) 
        if user is not None:  
            login(username,password)  
            return redirect('home') 
        else: 
            messages.error(request,'Invalid Username or Password')
            
    return render(request, 'login.html', {'form': form}) 

def custom_logout(request): 
    logout(request) 
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in after registration
            return redirect('home')  # Redirect to a home or login page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def productlist(request,categoryId=None): 
    if categoryId: 
        products=Product.objects.filter(categoryId=categoryId)  
    else: 
        products=Product.objects.all() 
    
    return render(request, 'productlist.html',{'products':products}) 

def productDetail(request,productId=None):
    if productId:
        details_of_product = get_object_or_404(Product, productId=productId)
        return render(request, 'productDetail.html', {'details_product': details_of_product})
    else:
        messages.error(request, "Please select the correct product")
        return redirect('productlist') 

@login_required
def merchant_dashboard(request):
    # Ensure the user is part of the merchant group
    if not request.user.groups.filter(name='Merchants').exists():
        # Redirect or show an error if the user is not a merchant
        return render(request, 'not_authorized.html')

    # Get data for the dashboard
    products = Product.objects.filter(merchant=request.user)  # Filter products by the logged-in merchant
    # Add more context data as needed

    return render(request, 'merchant/dashboard.html', {'products': products}) 
@login_required
def add_product(request): 
    if request.method=='POST': 
         form = ProductForm(request.POST, request.FILES)
         if form.is_valid(): 
             user= form.save(commit=False)
             Product.merchant=user
             Product.save()  
             return redirect('merchant-dashboard')
    else:
        form = ProductForm()

    return render(request, 'merchant/add_product.html', {'form': form}) 

@login_required 
def edit_product(request,Product_id): 
    product=get_object_or_404(Product,product_id=Product_id)
    if product.merchant==request.user:
        if request.method=='POST': 
            form = ProductForm(request.POST, request.FILES, instance=product) 
            if form.is_valid(): 
                form.save() 
                return redirect('merchant-dashboard')     
        else: 
            form = ProductForm(instance=product)    
    else: 
        messages.error("Merchant Mismatch") 
        return redirect('merchant-dashboard')
    return render(request, 'merchant/edit_product.html', {'form': form, 'product': product})

#def sales(request):
    
@login_required  # if the cart is user-specific
def view_cart(request):
    # Retrieve the user's cart based on the user ID
    user_cart = Cart.objects.get(user=request.user)
    items = user_cart.prod.all()  # Assuming the Cart model has a related field 'items'

    return render(request, 'cart.html', {'items': items})


    
            
            
            
        
        
    
    
       
    
# Create your views here.
