from django.contrib import admin
from django.urls import path
from restro_app import views


urlpatterns = [
    path('',views.home),
    path('menu/',views.menu,name='menu'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('mycart/',views.mycart,name='mycart'),
    path('addcart/<int:p_id>',views.addcart,name='addcart'),
    path('menuaddcart/<int:p_id>',views.menuaddcart,name='menuaddcart'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('dia/',views.dia,name='dia'),
    path('orderform/',views.orderform,name='orderform'),
    path('myorder/',views.myorder,name='myorder'),
]
