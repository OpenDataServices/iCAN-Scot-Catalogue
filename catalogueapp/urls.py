from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogueadmin', views.adminindex, name='adminindex'),
    path('service/<aliss_id>', views.service_index, name='service_index'),
    path('catalogueadmin/add', views.admin_add, name='admin_add'),
    path('catalogueadmin/list', views.admin_list, name='admin_list'),
    path('catalogueadmin/service/<aliss_id>', views.admin_service_index, name='admin_service_index'),
]
