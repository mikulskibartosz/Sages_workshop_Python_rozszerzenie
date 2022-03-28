"""
* Assignment: OOP Class Iris
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 2 min

English:
    1. Define class `Iris`
    2. Create instance `setosa` of a class `Iris`
    3. Create instance `virginica` of a class `Iris`
    4. Create instance `versicolor` of a class `Iris`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Iris`
    2. Stwórz instancję `setosa` klasy `Iris`
    3. Stwórz instancję `virginica` klasy `Iris`
    4. Stwórz instancję `versicolor` klasy `Iris`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Iris)
    >>> assert isinstance(setosa, Iris)
    >>> assert isinstance(versicolor, Iris)
    >>> assert isinstance(virginica, Iris)
"""


# Solution
class Iris:
    pass


setosa = Iris()
versicolor = Iris()
virginica = Iris()