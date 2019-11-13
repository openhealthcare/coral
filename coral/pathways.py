"""
Pathways for Coral
"""
import datetime

from opal.core.pathway import PagePathway, RedirectsToPatientMixin
from coral import models


class AddPatient(RedirectsToPatientMixin, PagePathway):
    display_name = "Add Patient"
    slug = "add_patient"
    icon = 'fa-plus'

    steps = [
        models.Demographics
    ]

    def save(self, *a, **k):
        patient, episode = super().save(*a, **k)
        episode.delete()
        return patient, episode
