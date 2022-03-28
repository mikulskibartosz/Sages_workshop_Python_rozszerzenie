"""
* Assignment: OOP Init Model
* Required: yes
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min
English:
    1. Model the data using classes Astronaut and SpaceAgency
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Create instances (watney, nasa) filling it with data
    3. Values must be passed at the initialization
    4. Create instances of a first class using positional arguments
    5. Create instances of a second class using keyword arguments
    6. Do not use `@dataclass`
    7. Run doctests - all must succeed
Polish:
    1. Zamodeluj dane za pomocą klas Astronaut i SpaceAgency
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Stwórz instancje (watney, nasa) wypełniając je danymi
    3. Wartości mają być podawane przy inicjalizacji
    4. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    5. Twórz instancje drugiej klasy używając argumentów nazwanych
    6. Nie używaj `@dataclass`
    7. Uruchom doctesty - wszystkie muszą się powieść
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
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


watney = Astronaut('Watney', 'USA', '1969-07-21')

nasa = SpaceAgency(name='NASA', country='USA', date='1958-07-29')