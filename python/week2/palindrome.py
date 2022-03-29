class Palindrome():
    def __init__(self):
        self.strArr = ["Do geese see God? ", "civic", "hello"]

    def __call__(self):
        for str in self.strArr:
            original = str
            str = str.strip()
            str = ''.join(char for char in str if char.isalnum())
            str = str.lower()

            if str == str[::-1]:
                print(original + " --> is a palindrome")
            else:
                print(original + " --> is not a palindrome")

def run():
  P = Palindrome()
  P()