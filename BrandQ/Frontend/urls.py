from django.urls import path

from Frontend import views

urlpatterns = [
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logindetail/', views.logindetail, name='logindetail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('homepage/', views.homepage, name='homepage'),

    path('search_result/', views.search_result, name='search_result'),
    path('search_re/<int:dat>/', views.search_re, name='search_re'),
    path('search_product_to_cart/', views.search_product_to_cart, name='search_product_to_cart'),

    path('productpage/<cat1>/', views.productpage, name='productpage'),
    path('productpage2/<cat2>/', views.productpage2, name='productpage2'),
    path('singleproduct/<int:data>/', views.singleproduct, name='singleproduct'),
    path('singleproduct2/<int:data1>/', views.singleproduct2, name='singleproduct2'),

    path('cartpage/', views.cartpage, name='cartpage'),
    path('cart2/', views.cart2, name='cart2'),
    path('cart_datas/', views.cart_datas, name='cart_datas'),
    path('delete_cart_data/<int:cartdata>/', views.delete_cart_data, name='delete_cart_data'),

    path('checkoutpage/', views.checkoutpage, name='checkoutpage'),
    path('order_address/', views.order_address, name='order_address'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('contact/', views.contact, name='contact'),
    path('contactdata/', views.contactdata, name='contactdata'),

]