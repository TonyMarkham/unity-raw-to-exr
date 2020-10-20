import os
from unity_raw_to_exr import raw_to_exr


def test_raw_to_ext():
    raw_to_exr("./tests/terrain-33.raw")
    assert os.path.exists("./tests/terrain-33.exr") == 1
