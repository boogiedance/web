from django.conf import settings

def media_context(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
