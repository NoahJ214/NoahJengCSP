def keypad():
  R = int(3)
  C = int(3)
  
  # Initialize matrix
  matrix = []
  print("Enter the entries rowwise:")
    
  # For user input
  for i in range(R):          # A for loop for row entries
      a =[]
      for j in range(C):      # A for loop for column entries
           a.append(input())
      matrix.append(a)
    
  # For printing the matrix
  for i in range(R):
      for j in range(C):
          print(matrix[i][j], end = " ")
      print()

def run():
    keypad()