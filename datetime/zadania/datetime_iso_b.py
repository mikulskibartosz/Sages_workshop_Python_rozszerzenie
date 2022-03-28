"""
* Assignment: Datetime ISO Parse
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min
English:
    1. Define `result: datetime` with converted `DATA` from ISO-8601
    2. Run doctests - all must succeed
Polish:
    1. Zdefiniuj `result: datetime` z przekonwertowaną `DATA` z ISO-8601
    2. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, must be a datetime'
    >>> result
    datetime.datetime(1969, 7, 21, 2, 56, 15, 123000)
"""

from datetime import datetime


DATA = '1969-07-21T02:56:15.123'

# datetime: DATA from ISO-8601 format
result = ...

