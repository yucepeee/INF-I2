
# P1.py
# This script performs basic arithmetic operations: addition, subtraction, multiplication, and division.

def add_numbers(a, b):
    """Add two numbers together.
      result devuelve el valor concatenado
      Parameters:
        a (int or float)
    """
    result = a + b
    return result


def sub_numbers(a, b):
    
    """Subtract two numbers.
      result devuelve el valor restado
    
      Parameters:
        a (int or float)
    """
    result = a - b
    return result


def mul_numbers(a, b):
    
    """Multiply two numbers.
      result devuelve el valor multiplicado

      Parameters:
        a (int or float)
    """
    result = a * b
    return result


def div_numbers(a, b):
    
    """Divide two numbers.
      result devuelve el valor dividido
      
      Parameters:
        a (int or float)
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = a / b
    return result


if __name__== "__main__":
  #solicita los valores de a y b
  a = int(input("Ingresa el valor de a: "))

  b = int(input("Ingresa el valor de b: "))

  #llama a las funciones y muestra los resultados
  print(f"La suma es: {add_numbers(a, b)}")

  print(f"La resta es: {sub_numbers(a, b)}")

  print(f"La multiplicación es: {mul_numbers(a, b)}")

  print(f"La división es: {div_numbers(a, b)}") 