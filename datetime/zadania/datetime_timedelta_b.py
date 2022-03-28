"""
* Assignment: Datetime Timedelta Age
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min
English:
    1. How old was Yuri Gagarin when he was launched to space?
    2. How old was Neil Armstrong when he made a first step on the Moon?
    3. Result round to full years
    4. Mind, that there are two different objects: `date` and `datetime`
    5. Run doctests - all must succeed
Polish:
    1. Ile miał lat Juri Gagarin kiedy wystartował w kosmos?
    2. Ile lat miał Neil Armstrong kiedy zrobił pierwszy krok na Księżycu?
    3. Rezultat zaokrąglij do pełnych lat
    4. Mind, that there are two different objects: `date` and `datetime`
    5. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(gagarin_age) is int, \
    'Variable `gagarin_age` has invalid type, must be a int'
    >>> assert type(armstrong_age) is int, \
    'Variable `armstrong_age` has invalid type, must be a int'
    >>> gagarin_age
    27
    >>> armstrong_age
    38
"""

from datetime import date, datetime


DAY = 1
MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY

GAGARIN_BIRTHDAY = date(1934, 3, 9)
GAGARIN_LAUNCH = datetime(1961, 4, 12, 6, 7)
ARMSTRONG_BIRTHDAY = date(1930, 8, 5)
ARMSTRONG_STEP = datetime(1969, 7, 21, 2, 56, 15)


# int: Gagarin's age when he was launched to space
gagarin_age = ...

# int: Armstrong's age when he made a first step on the Moon
armstrong_age = ...

