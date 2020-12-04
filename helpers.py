class distance:
    def __init__(self, meters):
        self._meters = meters

    def __repr__(self):
        return f"{self._meters:.2f} meters"

    @classmethod
    def from_centimeters(cls, centimeters):
        return cls(meters=centimeters * 0.01)

    @classmethod
    def from_inches(cls, inches):
        return cls(meters=inches / 39.37)

    def get_centimeters(self):
        return self._meters * 100

    def get_inches(self):
        return self._meters * 39.37
