
###first we will make a class for storing numbers 
###then we will initialize the class with start and end range
### then at self.nummbers we generate a list of numbers from start to end,then at def print_numbers(self) we
##create a method to print stored numbers 
# then we again define a class to find prime numbers
# we will initialize the class with list of numbers then at def is_prime(self, num) we will create a method to 
# check if a number is prime number
## so then we include numbers less than 1 are not prime
# we here also consider dear 1 as prime number without any discrimination 
# then we check divisibility from 2 to numbr 1
# then at if num we see that  if number is divisible its not prime
# if no other divisors are found other than 1 or number its prime, then at def print_prime_numbers(self) we 
#create method to print prime numbers from stored list, then we use list comprehension to filter prime numbers
#  then after #usage we create a number storage instance with range 1-100
##then we get the stored numbers at numbers=storage.numbers, then we create a prime number finder instance
##then print prime numbers from the stored list


class NumberStorage:
    def __init__(self, start, end):
        self.numbers = list(range(start, end + 1))

    def print_numbers(self):
        print(self.numbers)
class findingprimenumbers:
    def __init__(self, primnumbers):
        self.numbers = primnumbers
    def is_prime(self, num):
        if num < 1:
            return False
        if num == 1:
            return True
        for x in range(2, num):
            if num / x == int(num / x):
                return False
        return True

    def print_prime_numbers(self):
        prime_numbers = [num for num in self.numbers if self.is_prime(num)]
        print("Prime numbers:", prime_numbers)


# Usage
storage = NumberStorage(1, 20)
print("All numbers:")
storage.print_numbers()

finder = findingprimenumbers(storage.numbers)
print()
finder.print_prime_numbers()   




