from . import views
from django.urls import path
app_name='credentials'
urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('homepg',views.homepg,name='homepg'),
    path('details/',views.details,name='details'),
]