def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def check_primes_in_list(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers
        