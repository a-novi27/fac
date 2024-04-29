def test_fac(n):
    if n == 1:
        return 1
    return test_fac(n - 1) * n

print(test_fac(8))
