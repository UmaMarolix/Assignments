from django.urls import path
from compoundInterest.views import calculate

urlpatterns = [
    path('calculate/', calculate)
]
