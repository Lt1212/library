from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

#Add URL maps to redirect the base URL to our application

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]

# Use static() to add url mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Use include() to add URLS from the catalog application and authentication system

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

#
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)