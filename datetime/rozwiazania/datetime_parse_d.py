"""
* Assignment: Datetime Parse Many
* Complexity: medium
* Lines of code: 12 lines
* Time: 5 min
English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Run doctests - all must succeed
Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * `for ... in`
    * nested `try ... except`
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
     datetime.datetime(1961, 4, 12, 6, 7),
     datetime.datetime(1969, 7, 21, 2, 56, 15)]
"""

from datetime import datetime


DATA = [
    'Oct 4, 1957 19:28:34',  # Sputnik launch (first satellite in space)
    'April 12, 1961 6:07',  # Gagarin launch (first human in space)
    'July 21, 1969 2:56:15',  # Armstrong first step on the Moon
]

# list[datetime]: DATA elements in datetime format
result = ...

# Solution
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%b %d, %Y %H:%M:%S')
    except ValueError:
        try:
            dt = datetime.strptime(line, '%B %d, %Y %H:%M')
        except ValueError:
            dt = datetime.strptime(line, '%B %d, %Y %H:%M:%S')
    result.append(dt)


# Alternative Solution
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

result = [datetime.strptime(line, fmt)
          for line, fmt in zip(DATA, formats)]


# Alternative Solution
result = []
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

for line, fmt in zip(DATA, formats):
    x = datetime.strptime(line, fmt)
    result.append(x)


# Alternative Solution
result = []
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

for line in DATA:
    for fmt in formats:
        try:
            x = datetime.strptime(line, fmt)
        except ValueError:
            pass
        else:
            result.append(x)
            break
