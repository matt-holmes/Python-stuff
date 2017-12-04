# intlClient.py

from invoiceBuilder import InvoiceBuilder

class IntlClient(InvoiceBuilder):

    def apply_surcharge(self):
        self.total += 100.0

    def apply_discounts(self):
        for key, value in self.items.items():
            if key == "tech_support" and value > 1000:
                self.total *= .10
