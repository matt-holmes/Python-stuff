# domesticClient.py

from invoiceBuilder import InvoiceBuilder

class DomesticClient(InvoiceBuilder):

    def apply_surcharge(self):
        self.total += 25.0

    def apply_discounts(self):
        for key, value in self.items.items():
            if key == "customer_support" and value > 1000:
                self.total *= .10
