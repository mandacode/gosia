from django import forms

from works.models import Work


class CreateWorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['customer', 'employees', 'date', 'hours']
