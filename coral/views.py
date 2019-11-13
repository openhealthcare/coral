"""
Views for the Coral application
"""
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View
from opal.models import Patient


class CreateEpisodeView(LoginRequiredMixin, View):
    def post(self, *a, **k):
        patient_id = self.request.POST.get('patient_id')
        patient = Patient.objects.get(id=patient_id)
        patient.create_episode(start=datetime.date.today())
        return redirect('/#/patient/{}'.format(patient_id))
