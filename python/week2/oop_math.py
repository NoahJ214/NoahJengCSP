class fact:
  def __call__ (self, number):
      print("Factors of a Given Number {0} are:".format(number))
      for value in range(1, number + 1):
          if number % value == 0:
              print("{0}".format(value), end=" ")
      print()

def factors():
  fac = fact()
  print("hello from factors")
  num = int(input("Enter any Number to find its factors: "))
  fac(num)

if __name__ == "__main__":
  factors()