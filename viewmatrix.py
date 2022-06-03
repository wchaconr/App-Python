import os
import add

def view ():

  os.system("clear")
  
  isContinue = True
  while isContinue:
    
    print('Acceso para visualizar la lista de contactos')
    print(' ')
    print("_" * 50)
    print("    ")
    print("Presione 1 para buscar contacto por nombre o apellido o cédula")
    print("Presione 2 para ordenar contactos por ciclo (C1-C2-C3)")
    print("Presione 3 para finalizar")
    option = int(input('Opción... '))
    print("_" * 50)
    print("    ")
    
    if option != 1 and option != 2 and option != 3:
        print(' ')
        option = int(input('Eliga una opción válida... '))

    if option == 3:
        isContinue = False

    if option == 1:

      print("_" * 50)
      print("    ")
      user = input('Ingrese nombre, apellido o cédula del contacto: ')
      user = user.upper()
      print("_" * 50)
      print("    ")
    
      x=0
      for i in add.matrix:
        for j in i:
          if j == user:
            print('Contacto encontrado')
            print(' ')
            print(i)
            x=1
            print("    ")
            print("_" * 50)
            
      if x == 0:
        print('Contacto no encontrado encontrado en la base de datos')
        print('Presione 3 para finalizar: ')
        y=int(input('Opción ... '))
        isContinue = True
        if y == 3:
          isContinue = False

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 3:
        isContinue = False

    if option == 2:
      for i in add.matrix:
        for j in i:
          if j == 'C1':
            print(i)
      for i in add.matrix:
        for j in i:
          if j == 'C2':
            print(i)
      for i in add.matrix:
        for j in i:
          if j == 'C3':
            print(i)

      print(' ')
      print("*" * 50)
      print(' ')

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
          continue
      if rm == 3:
          isContinue = False
        
  os.system("clear")
  for i in add.matrix:
    print("    ")
    print("_" * 50)
    print(' ')
    print(i)  
    
  return