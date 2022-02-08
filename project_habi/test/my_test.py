import unittest
from core.real_states_service import RealStatesHandler


class TestsRealStateServiceMethods(unittest.TestCase):

    def test_get_request_service_real_states(self):
        """Test the request made to the service """
        response = [
            {"address": "calle 95 # 78 - 49",
             "description": "hermoso acabado, listo para estrenar",
             "price": 120000000, "city": "bogota", "state": 3},
            {"address": "calle 95 # 78 - 123",
             "description": "hermoso acabado, listo para estrenar",
             "price": 120000000, "city": "bogota", "state": 3}
            ]
        self.assertAlmostEqual(RealStatesHandler.do_GET(
            "http://127.0.0.1:8080/?city='bogota'&year=2020&state=3",
            response
            ))


if __name__ == '__main__':
    unittest.main()
