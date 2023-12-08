from django import forms

from .models import Scratchpad


class CreateScratchpadForm(forms.ModelForm):

    class Meta:
        model = Scratchpad
        fields = ['start_date', 'end_date']
