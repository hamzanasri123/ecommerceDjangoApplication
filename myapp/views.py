from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Product
import requests
# Create your views here.
def extract_products(api_response):
    """
    Fonction pour extraire les produits à partir de la réponse JSON de l'API.
    Cette fonction suppose que la structure JSON contient une liste de produits.
    Vous devrez ajuster cela en fonction du format réel de la réponse.

    Args:
        api_response (dict): La réponse JSON de l'API.

    Returns:
        list: Une liste d'objets représentant des produits.
    """
    products = []

    if 'products' in api_response:
        products_data = api_response['products']

        for product_data in products_data:
            product = Product(
                name=product_data.get('name', ''),
                price=product_data.get('price', 0),
                description=product_data.get('description', ''),
                # Ajoutez d'autres champs selon le format de vos produits
            )
            products.append(product)

    return products

def index(request):
    return render(request,"myapp/splash.html")


def listProduct(request):
    amazon_products = []
    products = Product.objects.all()
    # Appel à l'API Amazon
    url = "https://big-data-amazon.p.rapidapi.com/search/laptop"
    headers = {
        "X-RapidAPI-Key": "3bee7fbd2emsh17f024b15ac6cc1p18f35ejsnf02b93168e71",
        "X-RapidAPI-Host": "big-data-amazon.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()  # Vérifiez si la requête a échoué
        api_response = response.json()
        amazon_products = extract_products(api_response)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)    

    context = {
        'products': products
    }
    return render(request, 'myapp/index.html', context)


def detailProduct(request , id ) : 
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request , 'myapp/productDetail.html',context)

def addProduct(request):
    if request.method =="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('desc')
        image = request.FILES.get('upload')
        new_prod = Product(name=name, price=price, desc=description, image=image)
        new_prod.save()

    return render(request , 'myapp/addProduct.html')
    

def updateProduct(request , id ) :
    product = Product.objects.get(id=id)
    print(product)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES.get('upload')
        product.save()
        return redirect('/myapp/products')
    context = {
        "product" : product
    }
    return render(request,'myapp/updateProduct.html',context)


def deleteProduct(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    if request.method =="POST":
        product.delete()
        return redirect('/myapp/products')
  
    return render(request,'myapp/deleteProduct.html',context)
