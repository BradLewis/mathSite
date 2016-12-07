from django.conf.urls import url, include

urlpatterns = [
    url(r'^probcalc/', include('probcalc.urls')),
]
