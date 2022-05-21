from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

from .views import HomeView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    # path("", HomeView.as_view(), name="home"),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path(r'', include('cms.urls')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
