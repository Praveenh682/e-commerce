from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('fav_view',views.fav_view,name="fav_view"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collections',views.collections,name='collections'), 
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('checkout',views.checkout,name="checkout"),
    path('place_order',views.place_order,name="place_order"),
]