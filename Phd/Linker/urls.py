from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name = 'linker-home'),
    path('about/', views.about, name = 'linker-about'),
    path('dash/', login_required(views.dash), name = 'site-dash'),
    path('f404/', views.f404, name = 'f404'),
    path('table/', views.SensorDataListView.as_view(), name = 'sensorlist'),
]
