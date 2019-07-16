from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('', views.index,  name='index'),
    path('portfolio/<int:port_id>', views.portfolio, name='portfolio'),
    path('quote', views.quote, name='quote'),
]
