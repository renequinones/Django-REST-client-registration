from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Clients
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ClientsSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def clients_list(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        clients_serializer = ClientsSerializer(clients, many=True)
        return JSONResponse(clients_serializer.data)

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        clients_serializer = ClientsSerializer(data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JSONResponse(clients_serializer.data, \
                status=status.HTTP_201_CREATED)
        return JSONResponse(clients_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def clients_CRUD(request, pk):
    try:
        client = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clients_serializer = ClientsSerializer(client)
        return JSONResponse(clients_serializer.data)

    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        clients_serializer = ClientsSerializer(client, data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JSONResponse(clients_serializer.data)
        return JSONResponse(clients_serializer.errors, \
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)






def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                    'shop/product/list.html',
                    {'category': category,
                    'categories': categories,
                    'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
