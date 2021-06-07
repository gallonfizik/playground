from __future__ import annotations


class UnitSet:
    def __init__(self, unit_set: dict):
        self.unit_set = {}
        for k, v in unit_set.items():
            if v != 0:
                self.unit_set[k] = v

    def __repr__(self):
        return repr(self.unit_set)


class MinimumUnits:
    def __init__(self, units: list) -> None:
        self.units = units
        self.units.sort(reverse=True)
        self._smallest_unit_key = self._key(self.units[-1])

    def __call__(self, number: int) -> UnitSet:
        result = {}

        for _unit in self.units:
            if number == 0:
                break
            div, mod = divmod(number, _unit)
            number = mod
            result[self._key(_unit)] = div
        if number != 0:
            result[self._smallest_unit_key] = 1
        return UnitSet(result)

    def _key(self, unit: int):
        return str(unit)


class Totals:
    def __init__(self):
        self.totals = {}

    def add(self, material: str, unit_set: UnitSet):
        if material not in self.totals.keys():
            self.totals[material] = {}
        for k, v in unit_set.unit_set.items():
            if v == 0:
                pass
            if k not in self.totals[material].keys():
                self.totals[material][k] = v
            else:
                self.totals[material][k] = self.totals[material][k] + v


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
        },
        # {
        #     "metals": 2400,
        #     "ceramics": 7650
        # }
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
