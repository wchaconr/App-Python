import os
import add
import submenu as sb
#import numpy as np


def logIn():
  os.system("clear")
  print('Acceso para modificar o actualizar contactos')

  print(' ')

  print("_" * 50)
  print("    ")
  user = input('Ingrese la cédula del contacto a modificar: ')
  print("_" * 50)
  print("    ")

  x=0
  for i in add.matrix:
    for j in i:
      if j == user:
        print('Contacto encontrado')
        print(' ')
        print(i)
        var = i
        x=1
        
  if x == 0:
    print('Contacto no encontrado encontrado en la base de datos')
    print('Presione 7 para finalizar: ')
    y=int(input('Opción ... '))
  
    isContinue = True
    if y == 7:
      isContinue = False
  
  print("_" * 50)
  print("    ")
  print('Presione 0 para acceder a las opciones disponibles: ')
  print('Presione 7 para finalizar: ')
  y=int(input('Opción ... '))

  isContinue = True
  if y == 0:
    isContinue = True
  if y == 7:
    isContinue = False

    
  while isContinue:
    option = sb.submenu()
 
    if option !=1 and option !=2 and option !=3 and option !=4 and option !=5 and option !=6 and option !=7:
      print(' ')
      option = int(input('Eliga una opción válida... '))
    
    if option == 7:
      isContinue = False
  
    if option == 1:
      newname = input('Ingrese los nuevos nombres: ')
      newname = newname.upper()
      var[0] = newname
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False
  
    if option == 2:
      newsurname = input('Ingrese los nuevos apellidos: ')
      newsurname = newsurname.upper()
      var[1] = newsurname
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False

    if option == 3:
      newcc = input('Ingrese el nuevo número de cédula : ')
      var[2] = newcc
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False
  
    if option == 4:
      newgender = input('Ingrese el nuevo género: ')
      newgender = newgender.upper()
      var[3] = newgender
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False
  
    if option == 5:
      newage = input('Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ')
      var[4] = newage
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False
  
    if option == 6:
      newemail = input('Ingrese el nuevo correo: ')
      newemail = newemail.upper()
      var[5] = newemail
      print(var)

      print('Presione 0 para regresar al submenú de modificacion')
      print('Presione 7 para para finalizar')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 7:
        isContinue = False
      
        
#  add.matrix.append(var)
  for i in add.matrix:
    print(i)

  return 