from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from catalogueapp.forms import AddForm
from catalogueapp.tools import ALISS_URL, ALISS_Importer
from catalogueapp.models import Service


def index(request):
    context = {}
    return render(request, 'catalogueapp/index.html', context)


@permission_required('catalogueapp.catalogueadmin', login_url='/accounts/login/')
def adminindex(request):
    context = {}
    return render(request, 'catalogueapp/admin/index.html', context)


@permission_required('catalogueapp.catalogueadmin', login_url='/accounts/login/')
def admin_list(request):
    context = {
        'services': Service.objects.all(),
    }
    return render(request, 'catalogueapp/admin/list.html', context)


@permission_required('catalogueapp.catalogueadmin', login_url='/accounts/login/')
def admin_add(request):
    context = {}

    if request.method == 'POST':
        context['form'] = AddForm(request.POST)
        if context['form'].is_valid():
            url = ALISS_URL(context['form'].cleaned_data['url'])
            if url.is_service():
                importer = ALISS_Importer()
                service = importer.import_from_service_URL(url)
                print(service.id)
                print("DONE")
            else:
                context['form'].add_error('url', "That does not look like a service URL?")

    else:
        context['form'] = AddForm()

    return render(request, 'catalogueapp/admin/add.html', context)
