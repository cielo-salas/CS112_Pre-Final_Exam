# This program identifies the prime numbers in a given range
print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Cielo Salas")
print(''
      ''
      ''
      '')


def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


print(''
      ''
      ''
      '')

while True:
    start_num = int(input("Enter a number [start]: "))
    if start_num < 0:
        print("Enter a non-negative number.")
        continue
    end_num = int(input("Enter a number [end]: "))
    if end_num < 0:
        print("Enter a non-negative number.")
        continue
    if end_num < start_num:
        print("Enter a number greater than [start].")
        continue

    else:
        prime_numbers = get_primes_in_range(start_num, end_num)
        print("Prime numbers between", start_num, "and", end_num, "are:", prime_numbers)

    print(''
          ''
          ''
          '')
    option = int(input("Do you want to continue and do it again?"
                       "\n[1] Press 1 if yes"
                       "\n[0] Press 0 to exit"
                       "\nEnter here:"))
    if option == 1:
        print("You choose to continue.")
        continue
    elif option == 0:
        print("Program terminated.")
        break

