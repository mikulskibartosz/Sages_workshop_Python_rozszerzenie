"""
* Assignment: Generator Function Passwd
* Complexity: medium
* Lines of code: 10 lines
* Time: 8 min
English:
    1. Split `DATA` by lines and then by colon `:`
    2. Extract system accounts (users with UID [third field] is less than 1000)
    3. Return list of system account logins
    4. Implement solution using function
    5. Implement solution using generator and `yield` keyword
    6. Run doctests - all must succeed
Polish:
    1. Podziel `DATA` po liniach a następnie po dwukropku `:`
    2. Wyciągnij konta systemowe (użytkownicy z UID (trzecie pole) mniejszym niż 1000)
    3. Zwróć listę loginów użytkowników systemowych
    4. Zaimplementuj rozwiązanie wykorzystując funkcję
    5. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
    6. Uruchom doctesty - wszystkie muszą się powieść
Hints:
    * ``str.splitlines()``
    * ``str.split()``
    * unpacking expression
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isgeneratorfunction
    >>> assert isfunction(function)
    >>> assert isgeneratorfunction(generator)
    >>> list(function(DATA))
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
    >>> list(generator(DATA))
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
"""

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
lewis:x:1003:1002:Melissa Lewis:/home/ivanovic:/bin/bash"""


# Callable: list[str] with usernames when UID [third field] is less than 1000
def function(data: str):
    ...


# Generator: list[str] with usernames when UID [third field] is less than 1000
def generator(data: str):
    ...


