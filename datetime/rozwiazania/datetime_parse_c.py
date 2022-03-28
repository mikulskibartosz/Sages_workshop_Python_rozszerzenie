"""
* Assignment: Datetime Parse List
* Complexity: medium
* Lines of code: 8 lines
* Time: 5 min
English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Run doctests - all must succeed
Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * `for ... in`
    * `try ... except`
    * 24-hour clock
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'
    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [datetime.datetime(1957, 10, 4, 19, 28, 34),
    datetime.datetime(1961, 4, 12, 6, 7)]
"""

from datetime import datetime


DATA = [
    'Oct 4, 1957 19:28:34',  # Sputnik launch (first satellite in space)
    'April 12, 1961 6:07',  # Gagarin launch (first human in space)
]

# list[datetime]: parsed DATA
result = ...

# Solution
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%b %d, %Y %H:%M:%S')
    except ValueError:
        dt = datetime.strptime(line, '%B %d, %Y %H:%M')
    result.append(dt)