"""
* Assignment: Datetime Timedelta Period
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min
English:
    1. Given period is the time between Gagarin launch and Armstrong
       first step on the Moon:
        * 8 years
        * 3 months
        * 8 days
        * 20 hours
        * 49 minutes
        * 15 seconds
    2. Assume:
        a. year = 365.2425 days
        b. month = 30.436875 days
    3. Define `result: timedelta` representing given period
    4. Run doctests - all must succeed
Polish:
    1. Podany jest czas, który upłynął między startem Gagarina
       a pierwszym krokiem Armstronga na Księżycu:
        * 8 lat
        * 3 miesięcy
        * 8 dni
        * 20 godzin
        * 49 minut
        * 15 sekund
    2. Uwzględnij założenie:
        a. rok = 365.2425 dni
        b. miesiąc = 30.436875 dni
    3. Zdefiniuj `result: timedelta` reprezentujące dany okres
    4. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(result) is timedelta, \
    'Variable `result` has invalid type, must be a timedelta'
    >>> result
    datetime.timedelta(days=3022, seconds=10209)
"""

from datetime import timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY

# 8 years
# 3 months
# 8 days
# 20 hours
# 49 minutes
# 15 seconds

# timedelta: representing given period
result = ...

