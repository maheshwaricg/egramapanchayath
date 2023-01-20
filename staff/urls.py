from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home),
    path('logins/',views.loginstaff),
    path('staffpage/',views.staffpage),

]