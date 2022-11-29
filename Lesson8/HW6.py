def sumN(n):
    result = 0
    for i in range(n):
        result += i+1
    return result

def sumNCubes(n):
    result = 0
    for i in range(n):
        result += (i+1)**3
    return result


n = int(input('Enter your numbers:  '))
n_sum = sumN(n)
n_cube_sum = sumNCubes(n)
print("""The sum of the first {0} natural numbers is {1}.
The sum of their cubes is {2}.""".format(n, n_sum, n_cube_sum))


input()
