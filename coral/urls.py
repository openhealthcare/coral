from django.conf.urls import url
from django.urls import path
from opal.urls import urlpatterns as opatterns

from django.contrib import admin
admin.autodiscover()

from coral import views
from billing import views as billingviews

urlpatterns = [
    url(r'^create-new-episode', views.CreateEpisodeView.as_view(), name='create-new-episode'),
    path(
        'patient/<int:patient_id>/bill/create/',
        billingviews.BillCreateView.as_view(), name='create-bill'
    ),
    path(
        'patient/<int:patient_id>/billing-history/',
        billingviews.BillingHistoryView.as_view(), name='billing-history'
    ),
    path(
        'bill/<int:bill_id>/mark-paid/',
        billingviews.BillPaidView.as_view(), name="bill-paid"
    )
]

urlpatterns += opatterns
