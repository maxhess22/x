from django.urls import path
from .views import home,form



urlpatterns = [
    path('', home,name="index"),
    path('formulario', form, name="forma")
   
]
