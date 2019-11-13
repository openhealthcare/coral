"""
Context Processors for the Coral application
"""
from opal.core.subrecords import subrecords

def records(reuest):
    """
    Add a list of all non-singleton subrecords to context
    """
    show = [s for s in subrecords() if not s._is_singleton]
    show = [s for s in show if s.get_display_name() != 'Inpatient Admissions']
    return {
        'records': show
    }
