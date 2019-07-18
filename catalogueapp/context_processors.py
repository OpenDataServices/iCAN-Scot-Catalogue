from catalogueapp.models import ALISSMeta


def aliss_meta_processor(request):
    try:
        meta = ALISSMeta.objects.get()
    except ALISSMeta.DoesNotExist:
        meta = None
    return {'aliss_meta': meta}
