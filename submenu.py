import os
def submenu ():
  os.system("clear")
  print('Acceso par modificar o actualizar contactos')
  print(' ')
  print("*" * 50)
  print(' ')
  print('Presione 1 para modificar los nombres')
  print('Presione 2 para modificar los apellidos')
  print('Presione 3 para modificar la cédula')
  print('Presione 4 para modificar el género')
  print('Presione 5 para modificar la fecha de nacimiento')
  print('Presione 6 para modificar el correo')
  print('Presione 7 para finalizar')
  print('_' * 50)

  option = int(input('Opción ... ')) 
  return option