"""
* Assignment: Datetime ISO Format
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min
English:
    1. Define `result: str` with `DATA` converted to ISO-8601 format
    2. Run doctests - all must succeed
Polish:
    1. Zdefiniuj `result: str` z przekonwertowaną `DATA` do formatu ISO-8601
    2. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, must be a str'
    >>> result
    '1969-07-21T02:56:15'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

# datetime: DATA in ISO-8601 format: '1969-07-21T02:56:15'
result = ...

