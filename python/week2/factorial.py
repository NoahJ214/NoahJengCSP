
class factorial:
    def __call__(self, num):
      final = 1
      for i in range(1, num + 1):
        final = final * i
      return final

def factorial_run():
  fac = factorial()
  number = 144
  result = fac(number)
  print("The factorial of ", number, "is",   result)
  
  if __name__ == "__main__":
      factorial_run()