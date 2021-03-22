# Prime Number Calculation
n = int(input("Input a number: "))
def is_prime(number = n):
    factors = 0
    for i in range(1, number+1):
        if (number % i) == 0:
            print(i)
            print(number % i)
            factors += 1
        else:
            factors += 0
    if factors > 2:
        print(f"{number} its not a prime number")
    else:
        print(f"{number} its a prime number")

is_prime()
