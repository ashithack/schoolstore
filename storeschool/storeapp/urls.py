from django.urls import path
from . import views
app_name='storeapp'
urlpatterns = [
    path('',views.demo,name='demo'),


]