import requests

class PayPalInvoiceController:
    def __init__(self, api_token, vendor):
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
        }
        self.vendor = vendor

    def create_invoice(self):
        pass
        