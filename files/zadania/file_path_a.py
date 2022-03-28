"""
* Assignment: File Path Exception
* Required: yes
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min
English:
    1. Modify `result` function
    2. If `filename` exists, print 'Ok'
    3. If `filename` does not exist, print 'File not found'
    4. Run doctests - all must succeed
Polish:
    1. Zmodyfikuj funkcję `result`
    2. Jeżeli `filename` istnieje, wypisz 'Ok'
    3. Jeżeli `filename` nie istnieje, wypisz 'File not found'
    4. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * `try`
    * `except`
    * `else`
    * `open()`
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert isfunction(result), \
    'Variable `result` has invalid type, should be function'
    >>> result(__file__)
    Ok
    >>> result('_notexisting.txt')
    File not found
"""


def result(filename):
    ...
