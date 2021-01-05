from django.urls import path

from . import views

urlpatterns = [
    path('',views.Main),
    path('Profile', views.Profile_company),
    path('IB/', views.Income_balance),
    path('History/', views.History)
]