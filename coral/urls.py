from django.conf.urls import url
from opal.urls import urlpatterns as opatterns

from django.contrib import admin
admin.autodiscover()

from coral import views

urlpatterns = [
    url(r'^create-new-episode', views.CreateEpisodeView.as_view(), name='create-new-episode'),
]

urlpatterns += opatterns
