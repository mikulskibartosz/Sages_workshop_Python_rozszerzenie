"""
* Assignment: OOP InheritancePatterns Multilevel
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min
English:
    1. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    2. Use multilevel inheritance
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed
Polish:
    1. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    2. Użyj wielopoziomowego dziedziczenia
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    4. Uruchom doctesty - wszystkie muszą się powieść
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> assert isclass(Habitat)
    >>> assert isclass(Astronaut)
    >>> assert isclass(Rocket)
    >>> assert isclass(MarsMission)
    >>> assert issubclass(MarsMission, Habitat)
    >>> assert issubclass(MarsMission, Astronaut)
    >>> assert issubclass(MarsMission, Rocket)
    >>> assert len(Habitat.__subclasses__()) == 1
    >>> assert len(Astronaut.__subclasses__()) == 1
    >>> assert len(Rocket.__subclasses__()) == 1
    >>> assert len(MarsMission.__subclasses__()) == 0
"""


