"""
* Assignment: OOP Method Call
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min
English:
    1. Create instance of `Stats` class
    2. Iterate over `DATA` skipping header
    3. Separate features from label
    4. Call `mean()` method of `Stats` class passing list of features
    5. Define `result: list[float]` with list of means from each row
    6. Run doctests - all must succeed
Polish:
    1. Stwórz instancję klasy `Stats`
    2. Iteruj po `DATA` pomijając nagłówek
    3. Rozdziel cechy od etykiety
    4. Wywołuj metodę `mean()` klasy `Stats` przekazując listę features
    5. Zdefiniuj `result: list[float]` z listą średnich każdego z wierszy
    6. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * `round()`
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert type(result) is list
    >>> assert all(type(x) is float for x in result)
    >>> result
    [3.9, 2.5, 3.5, 4.1, 3.9, 2.4]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


class Stats:
    def mean(self, data):
        avg = sum(data) / len(data)
        return round(avg, 1)


# Solution
stats = Stats()
result = [stats.mean(X) for *X, y in DATA[1:]]