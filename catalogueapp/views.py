from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


def index(request):
    context = {}
    return render(request, 'catalogueapp/index.html', context)


@permission_required('catalogueapp.catalogueadmin', login_url='/accounts/login/')
def adminindex(request):
    context = {}
    return render(request, 'catalogueapp/admin/index.html', context)
