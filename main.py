# Desarollado por wilder chacón Rojas -  Gupo 41
import os
import add
import menu
import modify
import delete 
import viewmatrix as vm

isContinue = True

while isContinue:
    option = menu.menu()

    if option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        print(' ')
        option = int(input('Eliga una opción válida... '))

    if option == 5:
        isContinue = False

    if option == 1:
      add.createUsuario();
      for i in add.matrix:
        print(i)
      print(' ')
      print("*" * 50)
      print(' ')

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
        continue
      if rm == 5:
        isContinue = False

    if option == 2:
      modify.logIn()

      print(' ')
      print("*" * 50)
      print(' ')

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
          continue
      if rm == 5:
          isContinue = False

    if option == 3:
      delete.deleter()

      print(' ')
      print("*" * 50)
      print(' ')

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
          continue
      if rm == 5:
          isContinue = False

    if option == 4:
      vm.view()

      print(' ')
      print("*" * 50)
      print(' ')

      print('Presione 0 para regresar al menú principal')
      print('Presione 3 para salir de la plataforma')
      rm = int(input('Opción: '))

      if rm == 0:
          continue
      if rm == 5:
          isContinue = False

os.system("clear")
print('Hasta pronto')