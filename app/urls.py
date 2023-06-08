
from django.urls import  path 
from app import views

urlpatterns = [ 

    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('seller',views.handleseller,name='handleseller'),
     path('sellerlogin',views.handlesellerlogin,name='handlesellerlogin'),
]
    
   
