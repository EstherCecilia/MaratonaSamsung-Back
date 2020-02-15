from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path



urlpatterns = [
	url(r'^doencas/$', views.lista_labels, name='lista_doencas'),
	url(r'^salas/$', views.lista_terms, name='lista_salas'),
	url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
