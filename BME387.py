# Function to check if a number is prime
def is_prime(num):
    if num < 2:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:
            return False
    return True

# Loop through numbers 1 to 100
for number in range(1, 101):
    if is_prime(number):
        print(number)
        print("hello")
        
