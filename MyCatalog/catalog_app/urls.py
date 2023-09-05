from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('product_list', views.product_list, name='product list'),
    path('product_detail', views.product_detail, name='product detail'),
    path('register_account', views.register_account, name='register_account'),
    path('transfer', views.transfer, name='transfer'),

]