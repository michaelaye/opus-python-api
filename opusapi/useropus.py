from .opusapi import OPUSAPI
from query import Query, RangeQuery, MultQuery

translator = {"ISS": "Cassini ISS", "NAC": "Narrow Angle", "WAC": "Wide Angle"}


def example_search1():
    opus = OPUSAPI()
    opus.get_count(
        Query(
            RangeQuery("RINGGEOringradius", minimum=120_000, maximum=122_000),
            MultQuery("target", "Saturn Rings"),
            MultQuery("instrument", "Cassini ISS"),
            MultQuery("COISScamera", "Narrow Angle"),
        )
    )


def ringsearch(instrument="ISS_NAC", ringradius=(None, None)):
    """keep track of a popular search and for brainstorming

    Idea (maybe bad) is to separate instrument string by underscores IF/WHEN they have subfields
    and resolve them piece by piece with a translator dic? Possibly bad idea because of 
    overlapping values for NAC for different instruments?
    """

    # idea: if keyword value, like value of ringradius is tuple, then it HAS TO be
    # resolved with a RangeQuery, coorect?
    queries = []

    for token in instrument.split("_"):
        queries.append(MultQuery("instrument", token))
    # and this will fail because the next MultQuery needs an unknown field of COISScamera
    # I somehow wish that the field names BELOW an instrument query are not allowed to be
    # named instrument specific.
    # Specififcally, why is the field "COISScamera" not simply "camera"?
    # Because there is no nested namespace protection
    # like in Python, and the camera field name of a different instrument needs to be i
    # ts own unique identfier, even on a global level?


class USEROPUS:
    def __init__(self):
        self.opusapi = OPUSAPI()
        self.init_fields()

    def init_fields(self):
        self.fields = self.opusapi.fields

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        self._fields = value

    def search(self, target=None, instrument=None):
        pass
