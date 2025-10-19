import requests

class PayPalInvoiceController:
    def __init__(self, api_token, vendor, invoice_prefix, currency_code):
        self.invoice_api_url = "https://api-m.sandbox.paypal.com/v2/invoicing/invoices"
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
        }
        self.vendor = vendor
        self.invoice_prefix = invoice_prefix
        self.currency_code = currency_code

    def create_invoice(self, invoice_id):
        body = {

        }
        