
from django.contrib import admin
from django.urls import path
from app.views import index, add_hotel, delete, cyclical_add_hotel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_hotel/', add_hotel, name='add_hotel'),
    path('delete/', delete, name='delete'),
    path('cyclical_add_hotel/', cyclical_add_hotel, name='cyclical_add_hotel')
]
