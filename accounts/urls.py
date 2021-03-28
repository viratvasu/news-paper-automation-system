from django.urls import path
from .views import CreateCustomer,getInfo
urlpatterns = [
    path('create/customer',CreateCustomer.as_view()),
    path('get_info',getInfo.as_view()),
]
