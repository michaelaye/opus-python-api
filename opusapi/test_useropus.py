from .useropus import USEROPUS


def test_init():
    opus = USEROPUS()
    assert len(opus.fields) > 1