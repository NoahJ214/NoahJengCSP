class factorial:
  def __call__(self, num):
    final = 1
    for i in range(1, num + 1):
      final = final * i
    return final

factorial = factorial()
number = input("What # would you like to factorial?: ")
number = int(number)
print("The factorial of ", number, "is",   factorial(number))