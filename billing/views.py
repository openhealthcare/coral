"""
Views for the coral billing app
"""
from django.shortcuts import redirect
from django.utils.text import slugify
from django.views.generic import View, TemplateView, ListView
from opal.models import Patient

from billing.models import Bill, BillingItem


class BillCreateView(TemplateView):
    """
    View that allows users to create bills for patients
    """
    template_name = 'billing/bill_form.html'

    def dispatch(self, *a, **k):
        """
        Set self.patient
        """
        self.patient = Patient.objects.get(pk=k['patient_id'])
        return super().dispatch(*a, **k)

    def get_context_data(self, *a, **k):
        ctx = super().get_context_data(*a, **k)
        ctx['billing_items'] = BillingItem.objects.all()
        return ctx

    def post(self, *a, **k):
        bill = Bill(patient=self.patient)
        bill.save()

        for item in BillingItem.objects.all():
            slug = slugify(item.name)
            if self.request.POST.get(slug, False):
                bill.items.add(item)
        return redirect(self.patient.get_absolute_url())


class BillingHistoryView(ListView):
    """
    View that allows viewing of a patient's billing history.
    """
    model = Bill

    def get_queryset(self, *a, **k):
        patient      = Patient.objects.get(pk=self.kwargs['patient_id'])
        self.patient = patient
        return Bill.objects.filter(patient=patient)


class BillPaidView(View):
    """
    View that allows bills to be marked as paid
    """
    def post(self, *a, **k):
        bill = Bill.objects.get(pk=k['bill_id'])
        bill.paid = True
        bill.save()
        return redirect(bill.patient.get_absolute_url())
