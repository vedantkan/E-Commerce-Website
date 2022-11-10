from django.urls import path
from core.views import frontpage, shop, signup, myaccount, seller
from django.contrib.auth import views
from products.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name = 'signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name = 'login'),
    path('myaccount/', myaccount, name = 'myaccount'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('account/', seller, name='seller')
]