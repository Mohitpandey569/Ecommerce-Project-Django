from django.contrib import admin
from django.urls import path

from. import views
from .views import Home,deleteCartItems, viewCart,ProdDetailView,mobileFilter,laptopFilter,tvFilter,rangeView,sorting,search,addCart
urlpatterns = [
   path('',Home.as_view(),name="home"),
   path('prod_detail/<int:pk>',ProdDetailView.as_view(),name="prod_details"),
   path('mf/',mobileFilter,name="mf"),
   path('lf/',laptopFilter,name="lf"),
   path('tf/',tvFilter,name="tf"),
   path('rf/',rangeView,name="rf"),
   path('sort/',sorting,name="sort"),
   path('reg/',views.registerForm,name="reg"),
   path('search/',search,name="search"),
   path('cart/<int:id>',addCart,name="cart"),
   path('viewCart/',viewCart,name="viewCart"),
   path('deleteItem/<int:id>',deleteCartItems,name="deleteCart"),
   path('update_qty/<int:val>/<int:item_id>',views.updQty,name="update_qty"),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('place_orders',views.placeOrders,name="placeOrders"),
   path('payment/',views.makepayment,name='payment'),
   path('viewOrder/',views.viewOrder,name='viewOrder'),
   path('address/',views.address,name='address'),
   path('addaddress/',views.Addaddress,name='addaddress'),
   path('buy_now/<int:id>',views.buy_now,name='buy_now')
   #path("sendMail/",views.sendUserMail,name='sendMail'),
]
