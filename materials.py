from __future__ import annotations


class MinimumUnits:
    def __init__(self, units: list) -> None:
        self._units = units
        self._units.sort(reverse=True)
        self._smallest_unit = self._units[-1]
        self._smallest_unit_key = self._key(self._smallest_unit)

    def __call__(self, number: int) -> dict:
        result = {}

        for _unit in self._units:
            if number == 0:
                break
            div, mod = divmod(number, _unit)
            count_for_unit, number = self._get_count_for_unit_and_remainder(_unit, div, mod)
            if count_for_unit != 0:
                result[self._key(_unit)] = count_for_unit
        if number != 0:
            result[self._smallest_unit_key] = 1
        return result

    def _key(self, unit: int):
        return str(unit)

    def _get_count_for_unit_and_remainder(self, unit, div, remainder):
        if div == 0:
            return 0, remainder
        if (unit - remainder) < self._smallest_unit:
            return div + 1, 0
        else:
            return div, remainder


class Totals:
    def __init__(self):
        self.totals = {}

    def add(self, _material: str, units: dict):
        if _material not in self.totals.keys():
            self.totals[_material] = {}
        for k, v in units.items():
            assert (v != 0)
            if k not in self.totals[_material].keys():
                self.totals[_material][k] = v
            else:
                self.totals[_material][k] = self.totals[_material][k] + v


if __name__ == '__main__':
    minimum_units = {
        "metals": MinimumUnits([1000, 200, 50]),
        "ceramics": MinimumUnits([800, 320, 40])
    }

    requests = [
        {
            "metals": 2400,
            "ceramics": 7650
        },
        {
            "metals": 0,
            "ceramics": 9450-6776
        }
    ]

    totals = Totals()

    for request in requests:
        response = {}
        for material, request_for_material in request.items():
            minimum_unit_for_material = minimum_units[material](request_for_material)
            response[material] = minimum_unit_for_material
            totals.add(material, minimum_unit_for_material)
            print('{} {} <== {}'.format(material, request_for_material, minimum_unit_for_material))

    print('Totals: ')
    for material, total in totals.totals.items():
        print("{}: {}".format(material, repr(total)))
