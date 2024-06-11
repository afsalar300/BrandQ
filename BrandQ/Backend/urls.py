from django.contrib import admin
from django.urls import path

from Backend import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('Addcategory/', views.Addcategory, name='Addcategory'),
    path('categorydata/', views.categorydata, name='categorydata'),
    path('caytegorytable/', views.caytegorytable, name='caytegorytable'),
    path('cateEdit/<int:data1>/', views.cateEdit, name='cateEdit'),
    path('cateEditupdate/<int:data2>/', views.cateEditupdate, name='cateEditupdate'),
    path('deletecat/<int:cadata>/', views.deletecat, name='deletecat'),



    path('Addcategory2/', views.Addcategory2, name='Addcategory2'),
    path('categorydata2/', views.categorydata2, name='categorydata2'),
    path('categorytable2/', views.categorytable2, name='categorytable2'),
    path('cateEdit2/<int:data3>/', views.cateEdit2, name='cateEdit2'),
    path('cateEditupdate2/<int:data2>/', views.cateEditupdate2, name='cateEditupdate2'),
    path('deletecategory2/<int:categ2>/', views.deletecategory2, name='deletecategory2'),

    path('Addproduct/', views.Addproduct, name='Addproduct'),
    path('productdata/', views.productdata, name='productdata'),
    path('producttable/', views.producttable, name='producttable'),
    path('productedit/<int:data3>/', views.productedit, name='productedit'),
    path('productupdate/<int:data4>/', views.productupdate, name='productupdate'),
    path('prodelete/<int:prodata>/', views.prodelete, name='prodelete'),

    path('addproduct2/', views.addproduct2, name='addproduct2'),
    path('productdata2/', views.productdata2, name='productdata2'),
    path('Placed_order_detail/', views.Placed_order_detail, name='Placed_order_detail'),
]