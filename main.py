from controllers.DataBaseController import DataBaseContoller
from controllers.PayPalInvoiceController import PayPalInvoiceController
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    database = DataBaseContoller()
    invoice_manager = PayPalInvoiceController(os.getenv("PAYPAL_API_TOKEN"), os.getenv("VENDOR_NAME"))

if __name__ == "__main__":
    main()
        


