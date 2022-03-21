InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Noah",  
               "LastName": "Jeng",  
               "DOB": "Feb 14",  
               "Residence": "San Diego",  
               "Email": "nacjeng@gmail.com",  
               "Owns_Cars":["2005 Honda Odyssey", "2013 Honda Civic", "2014 Audi A6"]  
              })  

InfoDb.append({  
               "FirstName": "Tanay",  
               "LastName": "Rayavarapu",  
               "DOB": "Oct 10",  
               "Residence": "San Diego",  
               "Email": "tanayr@gmail.com",  
               "Owns_Cars":["2018 Audi A4","2020 Tesla Model 3","2004 Honda Pilot"]  
              })  

InfoDb.append({  
               "FirstName": "Joe",  
               "LastName": "Smith",  
               "DOB": "June 24",  
               "Residence": "New York",  
               "Email": "Joesmith@gmail.com",  
               "Owns_Cars":["Toyota", "Honda Civic", "Nissan"]  
              })  

InfoDb.append({  
               "FirstName": "Bob",  
               "LastName": "Jackson",  
               "DOB": "Dec 12",  
               "Residence": "Tokyo",  
               "Email": "bobjackson@gmail.com",  
               "Owns_Cars":["Chevy", "Mazda", "BMW"]  
              })  
# for loop iterates on length of InfoDb
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

def main():
  print("For loop: ")
  for_loop()
  print("While loop: ")
  while_loop(0)
  print("Recursive loop: ")
  recursive_loop(0)