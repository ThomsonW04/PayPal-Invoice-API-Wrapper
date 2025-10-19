from controllers.DataBaseController import DataBaseContoller
from controllers.PayPalInvoiceController import PayPalInvoiceController
from dotenv import load_dotenv
import os

load_dotenv()

class App:
    def __init__(self):
        self.database = DataBaseContoller()
        self.invoice_manager = PayPalInvoiceController(os.getenv("PAYPAL_API_TOKEN"), os.getenv("VENDOR_NAME"), os.getenv("INVOICE_PREFIX"), os.getenv("CURRENCY_CODE"))

    def create_local_invoice(self):
        last_tag = self.database.get_last_created_invoice()
        if last_tag is None:
            new_tag = 1
        else:
            new_tag = last_tag[0] + 1
        self.database.insert_new_invoice(new_tag)
        return new_tag

    def create_draft_invoice(self, invoice_tag):
        self.invoice_manager.create_invoice(invoice_tag)

def main():
    app = App()
    invoice_tag = app.create_local_invoice()
    app.create_draft_invoice(invoice_tag)

if __name__ == "__main__":
    main()
        


