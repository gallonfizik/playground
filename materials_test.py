import unittest

from materials import MinimumUnits


class MyTestCase(unittest.TestCase):
    def test_given_request_is_0_then_result_is_0(self):
        instance = self._instance()

        result = instance(0).totals

        for _, total in result.items():
            self.assertEqual(0, total.get())

    def test_given_request_is_less_than_minimum_unit_then_result_is_1(self):
        instance = self._instance()

        result = instance(2).totals

        self.assertEqual(0, result['100'].get())
        self.assertEqual(1, result['10'].get())

    def test_request_is_larger_than_maximum_unit(self):
        instance = self._instance()

        result = instance(234).totals

        self.assertEqual(2, result['100'].get())
        self.assertEqual(4, result['10'].get())

    def test_results_from_subsequent_calls_are_accumulated(self):
        instance = self._instance()

        # note that result is different than that from a call(510)
        result = instance(205)(305).totals

        self.assertEqual(5, result['100'].get())
        self.assertEqual(2, result['10'].get())

    def _instance(self):
        return MinimumUnits([10, 100])


if __name__ == '__main__':
    unittest.main()
