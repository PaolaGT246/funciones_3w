print(" ")
print("Gutierrez Torres Paola 3W")
print(" ")
#recursividad
def tri_recursion(k):
  if(k > 0): #si k es mayor que 0
    result = k + tri_recursion(k - 1) #funcion realiza suma
    print(result)#imprime resultado
  else:
    result = 0
  return result #regresa los valores del resultado

print("\n\nRecursion Example Results")
tri_recursion(6) #llamamos la funcion