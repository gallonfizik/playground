from __future__ import annotations


class Sum:
    def __init__(self) -> None:
        self.sum = 0

    def __call__(self, value: int) -> Sum:
        self.sum = self.sum + value
        return self

    def __repr__(self) -> str:
        return repr(self.sum)

    def get(self):
        return self.sum


class MinimumUnits:
    def __init__(self, units: list) -> None:
        self.units = units
        self.units.sort(reverse=True)
        self.totals = {}
        for _unit in units:
            self.totals[self._key(_unit)] = Sum()
        self._smallest_unit_key = self._key(self.units[-1])

    def __call__(self, number: int) -> MinimumUnits:
        for _unit in self.units:
            if number == 0:
                break
            div, mod = divmod(number, _unit)
            number = mod
            self.totals[self._key(_unit)](div)
        if number != 0:
            self.totals[self._smallest_unit_key](1)
        return self

    def __repr__(self):
        non_zero_sums = {}
        for k, v in self.totals.items():
            if v.get() != 0:
                non_zero_sums[k] = v
        return repr(non_zero_sums)

    def _key(self, unit: int):
        return str(unit)


if __name__ == '__main__':
    minimum_units = {
        "metals": MinimumUnits([1000, 200, 50]),
        "ceramics": MinimumUnits([800, 320, 40])
    }

    requests = {
        "metals": [3200 - 3000, 2880 - 2000],
        "ceramics": [2280 - 1600, 1]
    }

    for material, requests_for_material, accumulator in zip(requests.keys(), requests.values(), minimum_units.values()):
        for request in requests_for_material:
            accumulator(request)
        print("{}: {}".format(material, repr(accumulator)))
