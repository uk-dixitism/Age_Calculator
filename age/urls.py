from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('api/age/', views.AgeCalculate.as_view())
]