import os
import add
import numpy as np

def deleter():
  os.system("clear")
  print('Acceso para eliminar contactos')
  print(' ')
  print("_" * 50)
  print("    ")
  user = input('Ingrese la cédula del contacto que desea eliminar: ')
  print("_" * 50)
  print("    ")

  x=0
  for i in add.matrix:
    for j in i:
      if j == user:
        print('Contacto encontrado')
        print(' ')
        x = 1
        var = i
        print(var)
        print(' ')
        print("_" * 50)
        print("    ")
  print('Si desea eliminar este contacto presione 1: ')
  print('Si desea cancelar la opreación presione 0: ')
  confirm = int(input("Opcion ... "))
  if confirm == 1:
    arr = np.array(add.matrix)
    a = np.where(arr == user)
    b = a[0]
    add.matrix = np.delete(arr, b, axis=0)
    print(' ')
    print("_" * 50)
    print("    ")
    print('Usuario eliminado con éxito')
    for i in add.matrix:
      print(i)
    print(' ')
    print("_" * 50)
    print("    ")
  if x == 0:
    print('Contacto no encontrado encontrado en la base de datos')
        
  return      
