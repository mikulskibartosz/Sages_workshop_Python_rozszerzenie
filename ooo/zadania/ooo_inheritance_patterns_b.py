

"""
* Assignment: OOP InheritancePatterns Mixin
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min
English:
    1. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    2. Use mixins classes
    3. You can modify given classes
    4. Assignment demonstrates syntax, so do not add any attributes and methods
    5. Run doctests - all must succeed
Polish:
    1. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    2. Użyj klas domieszkowych (mixin)
    3. Możesz modyfikować dane klasy
    4. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    5. Uruchom doctesty - wszystkie muszą się powieść
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

