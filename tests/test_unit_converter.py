from sparrow.unit_converter import UnitConverter


def test_unit_converter():
    converter = UnitConverter([("h", 60, "m"), ("m", 60, "s"), ("s", 1000, "ms")])
    assert converter.query(("m", "ms", 1)) == 60000
    assert converter.query(("ms", "m", 60000)) == 1
    assert converter.query(("s", "ms", 1)) == 1000
    assert converter.query(("h", "m", 1)) == 60
    assert converter.query(("h", "s", 1)) == 3600
    assert converter.query(("h", "h", 1)) == 1
    assert converter.query(("hx", "h", 1)) is None
    assert converter.query(("h", "hx", 1)) is None
    assert converter.query(("hx", "hxx", 1)) is None
