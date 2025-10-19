import requests
import os
from dotenv import load_dotenv

load_dotenv()

class PayPalInvoiceManager:
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {os.getenv('PAYPAL_API_TOKEN')}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
        }
        self.vendor = os.getenv('VENDOR_NAME')

    def create_invoice(self, )
        


