from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from Market.views import *
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login"),
    path('logout/', logout_then_login, name='logout'),
    path('/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('product_list/', product_list, name='product_list'),
    path('<store_slug>/', product_list, name='product_list_by_store'),
    path('<id>/<slug>', product_detail, name='product_detail'),

]
