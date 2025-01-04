
def print_factors(n, m=2):
    if n % m == 0:
        print(f'{m}*', end='')
        print_factors(n/m)
    elif n > 1:
        print_factors(n, m+1)
        
print_factors(351)
        