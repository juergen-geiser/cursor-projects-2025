# factorial_simple.py

def factorial(n: int) -> int:
    """Berechnet n! für n >= 0.

    Raises:
        TypeError: wenn n kein int ist oder ein bool
        ValueError: wenn n < 0
    """
    # bool ist ein Subtyp von int -> explizit verbieten
    if isinstance(n, bool):
        raise TypeError("n muss ein int sein (bool ist nicht erlaubt)")

    if not isinstance(n, int):
        raise TypeError("n muss ein int sein")

    if n < 0:
        raise ValueError("n muss >= 0 sein")

    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


if __name__ == "__main__":
    # Beispielaufrufe (laufen nicht in Tests)
    print(factorial(0))   # 1
    print(factorial(5))   # 120
    print(factorial(10))  # 3628800


