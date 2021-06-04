# Who will pay the bill between us, ok ok don't fight. Let's find by aps.
import random
random_numbers = int(input("Enter some numbers: \n"))
random.seed(random_numbers)

persons = input("Entry everyones name: \n")
all_persons = persons.split(", ")
names = len(all_persons)

random = random.randint(0, names-1)
person_who_will_pay = all_persons[random]
print(f"{person_who_will_pay} will pay the bill today!")