# sieve of eratosthenes algorithms - The Sieve of Eratosthenes is a fast algorithm for finding all prime numbers up to a given number.
# sieve - Think of it like a filter: composite numbers (numbers with factors other than 1 and themselves) get filtered out, leaving only primes.

def sieveOfErtosthenes(num):
    # assume every number till num is prime
    all_number_till_num = [True] * (num + 1)

    # we know 0 and 1 us not considered as a prime number
    all_number_till_num[0] = False
    all_number_till_num[1] = False

    # start the number from 2
    p = 2

    while p*p <= num:
        if all_number_till_num[p]:
            # mark all the multiple of p as not prime
            for multiple in range(p*p , num+1 , p):
                all_number_till_num[multiple] = False
        p+=1
    
    # collect all the prime number from the all_number_till_num array
    prime_numbers = []
    for i in range(2 , num + 1):
        if all_number_till_num[i]:
            prime_numbers.append(i)
    
    return prime_numbers


if __name__ == "__main__":
    num = int(input("Enter any Number !"))
    print(sieveOfErtosthenes(num))