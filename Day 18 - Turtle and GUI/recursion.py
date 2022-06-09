def factorial_recursion(n):
    """Recursion: A function is calling itself again and again"""
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursion(n - 1)


f = factorial_recursion(0)
print(f)
lon = factorial_recursion(200)
print(lon)