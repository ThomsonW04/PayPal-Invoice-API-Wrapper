from controllers.DataBaseController import DataBaseContoller
from controllers.PayPalInvoiceController import PayPalInvoiceController
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = DataBaseContoller()
INVOICE_MANAGER = PayPalInvoiceController(os.getenv("PAYPAL_API_TOKEN"), os.getenv("VENDOR_NAME"))

def create_local_invoice():
    last_tag = DATABASE.get_last_created_invoice()
    if last_tag is None:
        new_tag = 1
    else:
        new_tag = last_tag[0] + 1
    DATABASE.insert_new_invoice(new_tag)
    return new_tag

def main():
    create_local_invoice()

if __name__ == "__main__":
    main()
        


