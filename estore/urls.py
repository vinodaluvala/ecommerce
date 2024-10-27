from django.urls import path
from estore import views

urlpatterns = [
    path('getproduct/search/', views.get_product, name='get_product'),
    path('createproduct/', views.create_product, name='create_product'),
    path('createcategory/', views.create_category, name='create_category'),
    path('updateproduct/', views.update_product, name='update_product'),
    path('getcategory/', views.get_category, name='get_category'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('getallproducts/', views.get_all_products, name='get_all_products'),
    path('updatecategory/', views.update_category, name='update_category'),

]