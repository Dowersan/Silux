from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('signup/', views.signup, name='signup'),
                  path('signin/', views.signin, name='signin'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
