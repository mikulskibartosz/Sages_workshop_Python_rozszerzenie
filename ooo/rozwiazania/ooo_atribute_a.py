"""
* Assignment: OOP Attribute Model
* Required: yes
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min
English:
    1. Model the data using classes Astronaut and SpaceAgency
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Create instances (watney, nasa) filling it with data
    3. How many classes are there?
    4. How many instances are there?
    5. Run doctests - all must succeed
Polish:
    1. Zamodeluj dane za pomocą klas Astronaut i SpaceAgency
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Stwórz instancje (watney, nasa) wypełniając je danymi
    3. Ile jest klas?
    4. Ile jest instancji?
    5. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in vars(watney).values()
    >>> assert 'USA' in vars(watney).values()
    >>> assert '1969-07-21' in vars(watney).values()
    >>> assert 'NASA' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1958-07-29' in vars(nasa).values()
"""


# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29


# Solution
class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
watney.name = 'Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa = SpaceAgency()
nasa.name = 'NASA'
nasa.country = 'USA'
nasa.date = '1958-07-29'