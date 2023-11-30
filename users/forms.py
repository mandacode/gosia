from django import forms

from .models import User, UserType


class UserForm(forms.ModelForm):

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    type = forms.ChoiceField(choices=UserType.choices)
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'type')

    def _set_initial_for_address_field(self, field_name):

        if not hasattr(self.instance, 'profile'):
            return

        if not self.instance.profile.address:
            return

        return getattr(self.instance.profile.address, field_name)

    def get_initial_for_field(self, field, field_name):

        if field_name == 'type':

            if not hasattr(self.instance, 'profile'):
                return UserType.EMPLOYEE

            return self.instance.profile.type

        if field_name in ['street_address', 'city', 'country', 'zip_code']:
            return self._set_initial_for_address_field(field_name)

        return super().get_initial_for_field(field, field_name)
