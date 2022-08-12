from django.shortcuts import render
from product.models import Product , Category
# Create your views here.

def home(request):
    
    all_category = Category.objects.all() 
    products = Product.objects.all()

    template = 'home.html'
    context = { 'all_category' : all_category , 'products' : products}

    return render(request , template , context)
    
def single1(request):
    return render(request, 'single1.html')
    
def single2(request):
    return render(request, 'single2.html')    
    
def single3(request):
    return render(request, 'single3.html')
    
def single4(request):
    return render(request, 'single4.html')
def single5(request):
    return render(request, 'single5.html')
def single6(request):
    return render(request, 'single6.html')    
    
def single7(request):
    return render(request, 'single7.html')    
    
def single8(request):
    return render(request, 'single8.html')    
    
def single9(request):
    return render(request, 'single9.html')    
    
def single10(request):
    return render(request, 'single10.html')    
    
def single11(request):
    return render(request, 'single11.html')    
    
def single12(request):
    return render(request, 'single12.html')
    
def single13(request):
    return render(request, 'single13.html')    
    
    
def single14(request):
    return render(request, 'single14.html')    
    
    
def single15(request):
    return render(request, 'single15.html')    
    
def single16(request):
    return render(request, 'single16.html')    
    
        
def single17(request):
    return render(request, 'single17.html')    
    
        
        
