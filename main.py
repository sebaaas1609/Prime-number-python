# Prime Number Calculation
n = int(input("Input a number: "))
def is_prime(number = n):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"{number} its a prime number")
    else:
        print(f"{number} its not a prime number")

is_prime()
