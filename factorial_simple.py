def factorial(n: int) -> int:
    """Berechnet n! für n >= 0."""
    if not isinstance(n, int):
        raise TypeError("n muss ein Integer sein")
    if n < 0:
        raise ValueError("n muss >= 0 sein")

    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

# Beispielaufrufe:
print(factorial(0))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800
