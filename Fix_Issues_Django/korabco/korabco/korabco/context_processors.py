from django.contrib.sites.models import Site


def get_site_url(request):
    return {
        'SITE_URL': request.scheme + '://' + Site.objects.get_current().domain,
    }
