from django.contrib import admin
from django.urls import path
from telegram.views import index
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import set_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', index),
    path('set-webhook/', set_webhook),
    path('', RedirectView.as_view(url='/admin')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
