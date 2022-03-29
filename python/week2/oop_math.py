class fact:
  def __call__ (self, number):
      print("Factors of a Given Number {0} are:".format(number))
      for value in range(1, number + 1):
          if number % value == 0:
              print("{0}".format(value), end=" ")
      print()

def factors():
  try:
    fac = fact()
    print("hello from factors")
    num = int(input("Enter any Number to find its factors: "))
    if num < 0:
      print("Input an integer equal to or greater than 0")
    fac(num)
  except ValueError:
    print("Input an integer")
