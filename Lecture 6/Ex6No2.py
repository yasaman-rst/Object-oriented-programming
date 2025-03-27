class Tool:
    def __init__(self, manufacturer, model, rpm):
        self._manufacturer = manufacturer
        self._model = model
        self._rpm = rpm

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model(self):
        return self._model

    @property
    def rpm(self):
        return self._rpm


class Drill(Tool):
    def __init__(self, manufacturer, model, rpm):
        super().__init__(manufacturer, model, rpm)
        self._drill_bits = []

    def attach_bit(self, bit):
        if isinstance(bit, DrillBit) and bit.diameter < 10:
            self._drill_bits.append(bit)
        else:
            raise ValueError("Bit diameter exceeds limit for cordless drill.")

    @property
    def drill_bits(self):
        return self._drill_bits


class DrillBit:
    def __init__(self, diameter, max_rpm):
        self._diameter = diameter
        self._max_rpm = max_rpm

    @property
    def diameter(self):
        return self._diameter

    @property
    def max_rpm(self):
        return self._max_rpm

cordless_drill = Drill("BrandX", "ModelY", 1500)
bit1 = DrillBit(9, 2000)
cordless_drill.attach_bit(bit1)
 #Print example
print(f"Drill: {cordless_drill.manufacturer} {cordless_drill.model}, RPM: {cordless_drill.rpm}")
for bit in cordless_drill.drill_bits:
    print(f"Attached Drill Bit: Diameter: {bit.diameter}mm, Max RPM: {bit.max_rpm}")
