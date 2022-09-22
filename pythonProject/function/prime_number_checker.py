def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime number\n")
    else:
        print("Its not a prime number\n")


n = int(input("Check this number\n"))
prime_checker(number=n)
