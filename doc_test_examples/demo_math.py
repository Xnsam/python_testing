"""Demo math example."""


def factor(n):
    """Return the faqctorial of n, an exact integer >= 0.

    >>> [factor(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factor(-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 6, in factor
    ValueError: n must be >= 0
    >>> factor(30.1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 8, in factor
    ValueError: n must be exact integer
    >>> factor(30.0)
    265252859812191058636308480000000
    >>> factor(1e100)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 10, in factor
    OverflowError: n too large
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
