from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from estore.models import category, product
from estore.serializers import categorySerializer, productSerializer
from django.http import HttpResponse
from estore.models import product, category


# Create your views here.
@api_view(['POST'])
def create_product(request):
    create_product = productSerializer(data=request.data)
    if create_product.is_valid():
        create_product.save()
        return Response(create_product.data, status=status.HTTP_201_CREATED)
    else:
        return Response(create_product.data, status=status.HTTP_400_BAD_REQUEST)

# API to search product with name
# search example - localhost:8000/api/getproduct/search/?name=curry leaves
@api_view(['GET'])
def get_product(request):
    search_query = request.query_params.get('name', None)
    if search_query:
        products = product.objects.filter(name__icontains=search_query)
        product_serializer = productSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "Please provide a search query with 'name' parameter."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_products(request):
    products = product.objects.all()
    product_serializer = productSerializer(products, many=True)
    return Response(product_serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request):
    updateproduct = productSerializer(data=request.data)
    if updateproduct.is_valid():
        updateproduct.save()
        return Response(updateproduct.data, status=status.HTTP_200_OK)
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product_delete = product.objects.get(pk=pk)
    except:
        return Response({"error": "Product does not exist."}, status=status.HTTP_400_BAD_REQUEST)
    product_delete.delete()
    return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_category(request):
    create_category = categorySerializer(data=request.data)
    if create_category.is_valid():
        create_category.save()
        return Response(create_category.data, status=status.HTTP_201_CREATED)
    else:
        return Response(create_category.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_category(request):
    categories = category.objects.all()
    category_serializer = categorySerializer(categories, many=True)
    return Response(category_serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_category(request, pk):
    updatecategory = categorySerializer(data=request.data)
    if updatecategory.is_valid():
        updatecategory.save()
        return Response(updatecategory.data, status=status.HTTP_200_OK)

