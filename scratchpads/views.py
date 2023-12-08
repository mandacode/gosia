import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from invoices.forms import CreateCustomerInvoiceForm
from invoices.services import create_customer_invoice
from .forms import CreateScratchpadForm
from .services import create_scratchpad, get_scratchpad, get_scratchpads

logger = logging.getLogger(__name__)


@login_required
def create_scratchpad_view(request):
    if request.method == 'POST':
        form = CreateScratchpadForm(request.POST)

        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            scratchpad = create_scratchpad(start_date, end_date)
            return redirect('scratchpads:detail', scratchpad_id=scratchpad.pk)

    else:
        form = CreateScratchpadForm()

    return render(request, 'scratchpads/create.html', {'form': form})


@login_required
def scratchpad_detail_view(request, scratchpad_id):
    scratchpad = get_scratchpad(scratchpad_id=scratchpad_id)
    return render(request, 'scratchpads/detail.html', {'scratchpad': scratchpad})


@login_required
def list_scratchpads_view(request):
    scratchpads = get_scratchpads()
    return render(request, 'scratchpads/list.html', {'scratchpads': scratchpads})


@login_required
def generate_customer_invoice_view(request, scratchpad_id):

    if request.method == 'POST':
        form = CreateCustomerInvoiceForm(request.POST)

        if form.is_valid():
            customer_id = form.cleaned_data['customer']
            invoice = create_customer_invoice(customer_id=customer_id, scratchpad_id=scratchpad_id)
            # return redirect('invoices:detail', invoice_id=invoice.pk)

    form = CreateCustomerInvoiceForm()

    return render(request, 'invoices/create.html', {'form': form})
