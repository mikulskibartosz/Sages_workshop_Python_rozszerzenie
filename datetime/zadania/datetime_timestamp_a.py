"""
* Assignment: Datetime Timestamp Limits
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min
English:
    1. Convert given dates to `datetime` objects
    2. Print timestamp for each date
    3. What is special about those dates?
    4. Run doctests - all must succeed
Polish:
    1. Przekonwertuj podane daty do obiektów `datetime`
    2. Wypisz timestamp każdej daty
    3. Co to za daty?
    4. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(a) is float, \
    '`a` must be a float object'
    >>> assert type(b) is float, \
    '`b` must be a float object'
    >>> assert type(c) is float, \
    '`c` must be a float object'
    >>> a
    -2115947647.0
    >>> b
    0.0
    >>> c
    2147483647.0
"""

from datetime import datetime


A = '1902-12-13T20:45:53+00:00'
B = '1970-01-01T00:00:00+00:00'
C = '2038-01-19T03:14:07+00:00'

# float: timestamp of A
a = ...

# float: timestamp of B
b = ...

# float: timestamp of C
c = ...

