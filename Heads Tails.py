print("/// Heads and Tails ///")
import random
numbers = int(input("enter mumbers: \n"))
random.seed(numbers)
random_numbers = random.randint(0, 1)

if random_numbers == 1:
    print("Heats")
else:
    print("Tails")