import os
def menu ():
  os.system("clear")
  print('**************************************************')
  print('Bienvenido a su plataforma de gestión de contactos')
  print('**************************************************')
  print('              por Wilder Chacón                   ')
  print(' ')
  print('                     MENÚ                         ')
  print(' ')
  print('Presione 1 para registrarse un nuevo contacto')
  print('Presione 2 para modificar o actualizar contactos')
  print('Presione 3 para eliminar contactos')
  print('Presione 4 para visualizar la lista de contactos')
  print('Presione 5 para salir de la plataforma')
  print(' ')
  x=int(input('opción... '))
  return x