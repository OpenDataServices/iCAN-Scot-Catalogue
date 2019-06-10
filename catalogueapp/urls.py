from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogueadmin', views.adminindex, name='adminindex'),
    path('catalogueadmin/add', views.admin_add, name='admin_add'),
]
