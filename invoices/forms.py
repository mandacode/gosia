from django import forms

from works.models import Customer, Employee


class CreateCustomerInvoiceForm(forms.Form):

    customer = forms.ChoiceField(choices=[], label='Select a customer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        scratchpad_id = kwargs.get('scratchpad_id')
        customers = list(Customer.objects.values_list('id', 'name'))
        self.fields['customer'].choices = customers


class CreateEmployeeInvoiceForm(forms.Form):

    employee = forms.ChoiceField(choices=[], label='Select an employee')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        scratchpad_id = kwargs.get('scratchpad_id')
        employees = list(Employee.objects.values_list('id', 'name'))
        self.fields['employee'].choices = employees
