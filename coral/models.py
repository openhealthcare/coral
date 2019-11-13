"""
coral models.
"""
from django.db.models import fields

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis):
        _angular_service = 'DiagnosisRecord'

class PastMedicalHistory(models.PastMedicalHistory):
    class Meta:
        verbose_name = "Past Medical History"

class Treatment(models.Treatment):
    _icon = "fa fa-circle"

class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""
