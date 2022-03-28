"""
* Assignment: Datetime Format US
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min
English:
    1. Define `result: str` with `DATA` in long US format
    2. Run doctests - all must succeed
Polish:
    1. Zdefiniuj `result: str` z `DATA` w długim formacie amerykańskim
    2. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, must be a str'
    >>> result
    'July 21, 1969 02:56:15 AM'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

# str: DATA in long US format: 'July 21, 1969 02:56:15 AM'
result = ...
