from __future__ import annotations

from minimum_units import MinimumUnits
from totals import Totals


class GameMinimumUnits:
    minimum_units = {
        "metals": MinimumUnits([1000, 200, 50]),
        "ceramics": MinimumUnits([800, 320, 40])
    }


class TripPlanner:
    def __init__(self):
        self._minimum_units = GameMinimumUnits.minimum_units
        self._totals = Totals()
        self._requests = []

    def road(self, metals: int, ceramics: int) -> TripPlanner:
        self._requests.append({'metals': metals, 'ceramics': ceramics})
        return self

    def print_layout(self):
        for request in self._requests:
            response = {}
            for material, request_for_material in request.items():
                minimum_unit_for_material = self._minimum_units[material](request_for_material)
                response[material] = minimum_unit_for_material
                self._totals.add(material, minimum_unit_for_material)
                print('{} {} <== {}'.format(material, request_for_material, minimum_unit_for_material))

        print('Totals: ')
        for material, total in self._totals:
            print("{}: {}".format(material, repr(total)))


if __name__ == '__main__':
    TripPlanner() \
        .road(2400, 7650) \
        .road(0, 9450 - 6776) \
        .print_layout()
