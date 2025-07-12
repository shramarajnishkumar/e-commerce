from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('men',views.men,name='men'),
    path('kid',views.kid,name='kid'),
    path('add',views.add,name='add'),
    path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('order',views.order,name='order'),
    path('login',views.login,name='login'),
    path('clogout',views.clogout,name='clogout'),
    path('cpassword',views.cpassword,name='cpassword'),
    path('cotp',views.cotp,name='cotp'),
    path('registration',views.registration,name='registration'),
    path('product_details/<int:pk>',views.product_details,name='product_details'),
    path('women',views.women,name='women'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('repass/',views.repass,name='repass'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('review/<int:pk>',views.review,name='review'),
    path('carts/',views.carts,name='carts'),
    path('deletecarts/<int:pk>',views.deletecarts,name='deletecarts'),
    path('checkout/',views.checkout,name='checkout'),
    path('order/',views.order,name='order'),






    

]