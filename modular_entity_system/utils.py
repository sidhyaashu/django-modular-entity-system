from django.http import Http404


def get_object_or_404(model, pk):

    try:
        return model.objects.get(pk=pk)

    except model.DoesNotExist:
        raise Http404(f"{model.__name__} not found")