from django.conf import settings # import the settings file


def media_root(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MEDIA_ROOT': settings.MEDIA_ROOT}