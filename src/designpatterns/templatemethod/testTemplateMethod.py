from invoiceBuilder import InvoiceBuilder
from intlClient import IntlClient
from domesticClient import DomesticClient
import unittest

class testTemplateMethod(unittest.TestCase):

    items1 = {"tech_support":5000.00, "customer_support":7500.0}
    items2 = {"tech_support":500.0, "customer_support":750.0}

    def test_calc_total(self):
        dc = DomesticClient()
        dc.calc_total(self.items1)
        self.assertEqual(dc.total, 1252.5)
        dc.calc_total(self.items2)
        self.assertEqual(dc.total, 1275.0)

        ic = IntlClient()
        ic.calc_total(self.items1)
        self.assertEqual(1260, ic.total)
        ic.calc_total(self.items2)
        self.assertEqual(1350, ic.total)

if __name__ == '__main__':
    unittest.main()
