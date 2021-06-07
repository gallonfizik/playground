import unittest

from materials import MinimumUnits


class MyTestCase(unittest.TestCase):
    def test_given_request_is_0_then_result_is_0(self):
        instance = self._instance()

        result = instance(0)

        for _, total in result.items():
            self.assertEqual(0, total.get())

    def test_given_request_is_less_than_minimum_unit_then_result_is_1(self):
        instance = self._instance()

        result = instance(2)

        self.assertNotIn('100', result.keys())
        self.assertEqual(1, result['10'])

    def test_request_is_larger_than_maximum_unit(self):
        instance = self._instance()

        result = instance(234)

        self.assertEqual(2, result['100'])
        self.assertEqual(4, result['10'])

    def test_use_larger_unit_if_remainder_is_less_than_smallest_unit(self):
        instance = self._instance()

        result = instance(191)

        self.assertEqual(2, result['100'])
        self.assertNotIn('10', result)

    def _instance(self):
        return MinimumUnits([10, 100])


if __name__ == '__main__':
    unittest.main()
