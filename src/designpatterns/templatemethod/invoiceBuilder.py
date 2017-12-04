#invoicebuilder.py

import abc

class InvoiceBuilder(metaclass=abc.ABCMeta):

    def calc_total(self, items):
        self.items = items
        self.total = 0.0
        self.calc_total_services()
        self.apply_surcharge()
        self.apply_discounts()

    def calc_total_services(self):
        for key, value in self.items.items():
            self.total += value

    @abc.abstractmethod
    def apply_surcharge(self):
        pass

    @abc.abstractmethod
    def apply_discounts(self):
        pass
