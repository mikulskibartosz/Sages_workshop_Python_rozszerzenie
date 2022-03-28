"""
* Assignment: OOP Stringify Nested
* Required: yes
* Complexity: medium
* Lines of code: 9 lines
* Time: 21 min
English:
    1. Overload `str` and `repr` to achieve desired printing output
    2. Run doctests - all must succeed
Polish:
    1. Przeciąż `str` i `repr` aby osiągnąć oczekiwany rezultat wypisywania
    2. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * Define `Crew.__str__()`
    * Define `Astronaut.__str__()` and `Astronaut.__repr__()`
    * Define `Mission.__repr__()`
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> melissa = Astronaut('Melissa Lewis')
    >>> print(f'Commander: \\n{melissa}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Commander:
    Melissa Lewis
    >>> mark = Astronaut('Mark Watney', experience=[
    ...     Mission(2035, 'Ares 3')])
    >>> print(f'Space Pirate: \\n{mark}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Space Pirate:
    Mark Watney veteran of [
          2035: Ares 3]
    >>> crew = Crew([
    ...     Astronaut('Mellisa Lewis', experience=[
    ...         Mission(2031, 'Ares 1'),
    ...         Mission(2035, 'Ares 3'),
    ...     ]),
    ...     Astronaut('Mark Watney', experience=[
    ...         Mission(2035, 'Ares 3'),
    ...     ]),
    ...     Astronaut('Rick Martinez'),
    ... ])
    >>> print(f'Crew: \\n{crew}')  # doctest: +NORMALIZE_WHITESPACE
    Crew:
    Mellisa Lewis veteran of [
          2031: Ares 1,
          2035: Ares 3]
    Mark Watney veteran of [
          2035: Ares 3]
    Rick Martinez
"""


class Crew:
    def __init__(self, members=()):
        self.members = list(members)


class Astronaut:
    def __init__(self, name, experience=()):
        self.name = name
        self.experience = list(experience)


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name
