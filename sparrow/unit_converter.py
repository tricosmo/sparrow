from typing import Optional


class UnitConverter:
    def __init__(self, factors: list):
        """Why there is a fucking tab."""

        self.unit_mappers = {}
        for from_unit, rate, to_unit in factors:
            self.unit_mappers[from_unit] = [to_unit, rate]

    def get_rate(self, from_unit: str, to_unit: str) -> Optional[float]:
        if from_unit not in self.unit_mappers:
            return None
        rate = 1
        while True:
            try:
                to_, convertion = self.unit_mappers[from_unit]
            except KeyError:
                return None
            if to_ == to_unit:
                return rate * convertion

            rate *= convertion
            from_unit = to_

    def query(self, query_param: list) -> Optional[float]:
        from_unit, to_unit, quantity = query_param
        if from_unit == to_unit:
            return quantity
        rate = self.get_rate(from_unit, to_unit)
        if rate:
            return rate * quantity
        rate = self.get_rate(to_unit, from_unit)
        if rate:
            return quantity / rate
        return None
