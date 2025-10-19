import requests

class PayPalInvoiceController:
    def __init__(self, api_token, vendor, invoice_prefix):
        self.invoice_prefix = invoice_prefix
        self.invoice_api_url = "https://api-m.sandbox.paypal.com/v2/invoicing/invoices"
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
        }
        self.vendor = vendor

    def create_invoice(self, invoice_id):
        body = {

        }
        