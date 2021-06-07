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
