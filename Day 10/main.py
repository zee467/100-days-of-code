from art import logo

# Assume the code is running in a replit environment
# from replit import clear


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  if n2 == 0:
    return "ZeroDivisionError"

  return n1 / n2

operations = { 
  "+": add, 
  "-": subtract,
  "*": multiply, 
  "/": divide
}

def calc(operator, f_num, s_num):
  operation_func = operations[operator]
  return operation_func(f_num, s_num)

def start_anew():
  print(logo)
  f_num = float(input("What's your first number?: "))
  for symbol in operations:
      print(symbol)

  return f_num

first_num = start_anew()

continue_cal = True
while continue_cal:   
    operation = input("Pick an operation: ")
    second_num = float(input("What's your next number?: "))
    total = calc(operation, first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {total}")

    proceed_with_prior = input(f"Type 'y' to continue calculating with {total} or type 'n' to start a new calculation: ").strip().lower()
    if proceed_with_prior == "y":
      first_num = total
    else:
    #   clear()
      print("\n\n\n\n\n\n\n\n\n\n\n")
      start_anew()
      

      
      

