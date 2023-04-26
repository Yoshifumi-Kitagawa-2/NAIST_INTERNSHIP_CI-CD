import unittest
from NAIST_lecture_CI_CD.CSVPrinter import CSVPrinter

def setUpModule():
    print('Running setUpModule')
def tearDownModule():
    print('Running tearDownModule')

class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")
    def setUp(self):
        print("Running setUp")
    def tearDown(self):
        print("Running tearDown")
    def test_read_1(self):
        print("Ruuning test_read_1")
        printer = CSVPrinter("./sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
    def test_read_2(self):
        print("Ruuning test_read_2")
        printer = CSVPrinter("./sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l[0]))