from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
