class Totals:
    def __init__(self):
        self.totals = {}

    def add(self, _material: str, units: dict):
        if _material not in self.totals.keys():
            self.totals[_material] = {}
        for unit, amount in units.items():
            assert (amount != 0)
            if unit not in self.totals[_material].keys():
                self.totals[_material][unit] = amount
            else:
                self.totals[_material][unit] = self.totals[_material][unit] + amount

    def __iter__(self):
        return iter(self.totals.items())