import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models import Sum

from invoices.generator.services import generate_customer_invoice
from scratchpads.models import Scratchpad
from works.models import Customer


def create_customer_invoice(customer_id: int, scratchpad_id: int):

    scratchpad = Scratchpad.objects.get(pk=scratchpad_id)
    customer = Customer.objects.get(pk=customer_id)
    manager = User.objects.get(email='goshia71@interia.pl')
    today = datetime.date.today()
    location_and_date = f"Berlin, den {today.strftime('%d.%m.%Y')}"

    invoice_number = f"{today.year}/{scratchpad_id}"  # edit this line to use a real invoice number
    header = f"Rechnungsnummer: {invoice_number}"
    recipient = f"\n{customer.name}\n{customer.address.street_address}\n{customer.address.zip_code} {customer.address.city}"
    sender = f"{manager.first_name} {manager.last_name}\n{manager.profile.address.street_address}\n{manager.profile.address.zip_code} {manager.profile.address.city}\nTel. Pl. {manager.profile.phone_number}"
    text = f"Sehr geehrte Herr {customer.name.split()[-1]},\n\nwir haben für Sie Reinigungsarbeiten in Ihrem Haushalt erbracht. Die Abrechnung entnehmen Sie bitte der beigefügten Aufstellung"

    records = scratchpad.records.filter(customer=customer)
    grouped = records.values('date').annotate(
        hours_amount=Sum('hours'),
        total_price=Sum('hours') * customer.hourly_rate
    )
    worked_hours = [[record['date'].strftime('%d.%m.%Y'), f"{record['hours_amount']} Std", f"{record['total_price']:.2f} €"] for record in grouped]

    netto = sum([record['total_price'] for record in grouped])
    tax = round(netto * Decimal(0.19), 2)
    brutto = netto + tax
    signature = f"Bitte überweisen Sie den Gesamtbetrag innerhalb von 10 Tagen auf folgendes Konto:\n\nBank: {manager.profile.bank_account.bank_name}\nIBAN: {manager.profile.bank_account.iban}\nBIC: {manager.profile.bank_account.bic}\n\nVielen Dank für Ihren Auftrag!"
    footer = f"Mit freundlichen Grüßen\n\n{manager.get_full_name()}"

    data = {
        "header": header,
        "location_and_date": location_and_date,
        "recipient": recipient,
        "sender": sender,
        "text": text,
        "worked_hours": worked_hours,
        "netto": f"{netto} €",
        "tax": f"{tax} €",
        "brutto": f"{brutto} €",
        "signature": signature,
        "footer": footer
    }

    generate_customer_invoice(data=data)
