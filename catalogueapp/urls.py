from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogueadmin', views.adminindex, name='adminindex'),
    path('organisation/<aliss_id>', views.organisation_index, name='organisation_index'),
    path('catalogueadmin/add', views.admin_add, name='admin_add'),
    path('catalogueadmin/service', views.admin_service_list, name='admin_service_list'),
    path('catalogueadmin/service/<aliss_id>', views.admin_service_index, name='admin_service_index'),
    path('catalogueadmin/organisation', views.admin_organisation_list, name='admin_organisation_list'),
    path('catalogueadmin/organisation/<aliss_id>', views.admin_organisation_index, name='admin_organisation_index'),
    path('accounts/profile/', views.user_profile, name='user_profile'),

]
