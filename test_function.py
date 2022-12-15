import timeit

def fac_recursive(n):
  return 1 if (n==1 or n==0) else n * fac_recursive(n - 1)

def fac_iterative(n):
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result

n = 100

print("Recursive implementation:")
print(timeit.timeit(lambda: fac_recursive(n), number=1))

print("Iterative implementation:")
print(timeit.timeit(lambda: fac_iterative(n), number=1))
