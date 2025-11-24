def is_it_even (number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

number = int(input("Enter a number: "))
result = is_it_even(number)
print(f"The number {number} is {result}")
