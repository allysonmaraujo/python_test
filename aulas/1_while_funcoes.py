def sum(a,b):
  return a+b

def sub(a,b):
  return a-b

def div(a,b):
  return a/b

def mul(a,b):
  return a*b

print("Escolha uma das opções:")
print("1. somar")
print("2. subtrair")
print("3. dividir")
print("4. multiplicar")

while True:
  choice = input("Digite sua escolha 1/2/3/4: ")
  if choice in ('1', '2', '3', '4'):

    a = float(input("Coloque o primeiro numero: "))
    b = float(input("Coloque o segundo numero: "))

    if choice == '1':
      print(a, "+", b, "=", sum(a,b))
    elif choice == '2':
      print(a, "-", b, "=", sub(a,b))
    elif choice == '3':
      print(a, "/", b, "=", div(a,b))
    elif choice == '4':
      print(a, "*", b, "=", mul(a,b))
    break
  else:
    print("Invalid Input")