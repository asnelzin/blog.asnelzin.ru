from django.conf import settings


def settings_context(request):
    return {'is_debug': settings.DEBUG}