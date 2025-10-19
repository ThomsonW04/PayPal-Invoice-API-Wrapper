import requests

class PayPalInvoiceController:
    def __init__(self, api_token, vendor_given_names, vendor_last_names, vendor_email, invoice_prefix, currency_code):
        self.invoice_api_url = "https://api-m.sandbox.paypal.com/v2/invoicing/invoices"
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
        }
        self.vendor_given_names = vendor_given_names
        self.vendor_last_names = vendor_last_names
        self.vendor_email = vendor_email
        self.invoice_prefix = invoice_prefix
        self.currency_code = currency_code

    def create_invoice(self, invoice_id, note):
        body = {
            "detail": {
                "invoice_number": self.invoice_prefix + invoice_id,
                "currency_code": self.currency_code,
                "note": note
            }
        }
        