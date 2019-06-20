import unittest

from parking_app.parking_lot import ParkingLot
from parking_app.processor import Processor
from parking_app.search_parking import SearchParking


class TestBase(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()
        self.parking = ParkingLot()
        self.search_parking = SearchParking(
            parking=self.parking
        )

    def tearDown(self):
        self.processor = None
        self.parking = None
        self.search_parking = None
