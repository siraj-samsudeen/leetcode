# Introduction to Problem Solving - Class | Scaler Academy
# https://www.scaler.com/academy/mentee-dashboard/class/11074/session?joinSession=1

# find whether a number is a prime number or not
# prime number has EXACTLY 2 factor - 1 and itself
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

assert isPrime(2) == True
assert isPrime(3) == True
assert isPrime(13) == True

assert isPrime(4) == False
assert isPrime(12) == False

assert isPrime(1) == False

# use the idea that a and N/a are the 2 factors of N which start repeating after a point
def isPrime(n):
    if n <=1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0: 
            print(f"{i} is a divisor of {n}")
            return False
    print(f"No divisor upto {i} for {n}")
    return True

# optimize even more
import math
def isPrime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    
    # this will eliminate all even numbers at one go
    if n % 2 == 0:
        return False
    # we start at odd number 3, so step size is 2 so that we cover only odd numbers
    for i in range(3, math.isqrt(n) + 1, 2):
        if i * i > n:
            break
        if n % i == 0: 
            print(f"{i} is a divisor of {n}")
            return False
    print(f"No divisor upto {i} for {n}")
    return True

assert isPrime(123) == False
assert isPrime(127) == True

# basic algo
def sqrt(n):
    for i in range(n):
        if i * i == n:
            return i

# use binary search logic to reduce search space by half
def sqrt(n):
    low, high = 1, n

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            high = mid - 1
        else:
            low = mid + 1

