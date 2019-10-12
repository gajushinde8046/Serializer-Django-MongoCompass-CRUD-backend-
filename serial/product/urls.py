
from django.urls import path
from .views import *


urlpatterns = [
    path('get/', getlist),
   # path('get_getadmin/<str:name>',get_getadmin)
    # path('get/<str:name>', get)
    # path('justget/', justget)
    path('details/<str:productName>/',getdetails)
]
