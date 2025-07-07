from django import forms
from .models import Todo
from django.utils.timezone import get_current_timezone
from zoneinfo import ZoneInfo
import zoneinfo

class TodoForm(forms.ModelForm):
    timezone = forms.ChoiceField(
        choices=[(tz, tz) for tz in sorted(zoneinfo.available_timezones())],
        initial='America/Caracas',
        label="Zona Horaria"
    )
    
    class Meta:
        model = Todo
        fields = ['title', 'details', 'timezone']