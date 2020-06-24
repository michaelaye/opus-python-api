import pandas as pd

from opusapi import *

O = OPUSAPI()

f = O.get_raw_fields()
print('*** Raw Fields as Dict:')
print('Multiple:')
print(f['target'])
print()
print('String:')
print(f['volumeid'])
print()
print('Single-column range:')
print(f['observationduration'])
print()
print('Two-column range:')
print(f['RINGGEOringradius1'])
print(f['RINGGEOringradius2'])
print()
print()

rdf = O.get_raw_fields_as_df()
print('*** Raw Fields as DataFrame:')
print(rdf)
print('Multiple:')
print(rdf.loc['target'])
print()
print('String:')
print(rdf.loc['volumeid'])
print()
print('Single-column range:')
print(rdf.loc['observationduration'])
print()
print('Two-column range:')
print(rdf.loc['RINGGEOringradius1'])
print(rdf.loc['RINGGEOringradius2'])
print()
print()

f = O.get_fields()
print('*** Fields as Dict:')
print('Multiple:')
print(f['target'])
print()
print('String:')
print(f['volumeid'])
print()
print('Single-column range:')
print(f['observationduration'])
print()
print('Two-column range:')
print(f['RINGGEOringradius'])
print()
print()

df = O.get_fields_as_df()
print('*** Fields as DataFrame:')
print(df)
print('Multiple:')
print(df.loc['target'])
print()
print('String:')
print(df.loc['volumeid'])
print()
print('Single-column range:')
print(df.loc['observationduration'])
print()
print('Two-column range:')
print(df.loc['RINGGEOringradius'])
print()
print()
