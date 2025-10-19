from controllers.DataBaseController import DataBaseContoller
from controllers.PayPalInvoiceController import PayPalInvoiceController
from dotenv import load_dotenv
import os

load_dotenv()

class App:
    def __init__(self):
        self.database = DataBaseContoller()
        self.invoice_manager = PayPalInvoiceController(api_token = os.getenv("PAYPAL_API_TOKEN"), 
                                                       vendor_given_names = os.getenv("VENDOR_GIVEN_NAMES"), 
                                                       vendor_last_names = os.getenv("VENDOR_LAST_NAMES"), 
                                                       vendor_email = os.getenv("VENDOR_EMAIL"), 
                                                       invoice_prefix = os.getenv("INVOICE_PREFIX"), 
                                                       currency_code = os.getenv("CURRENCY_CODE"))

    def create_local_invoice(self):
        last_tag = self.database.get_last_created_invoice()
        if last_tag is None:
            new_tag = 1
        else:
            new_tag = last_tag[0] + 1
        self.database.insert_new_invoice(new_tag)
        return new_tag

    def create_draft_invoice(self, invoice_tag, note, customer_email, item):
        response = self.invoice_manager.create_invoice(invoice_tag, note, customer_email, item)
        print(response)

def main():
    app = App()
    invoice_tag = app.create_local_invoice()
    app.create_draft_invoice(invoice_tag, "Pleasure doing business.", "melissajadeclark10@gmail.com", {"name": "Living", "value": "50.00"})

if __name__ == "__main__":
    main()
        


