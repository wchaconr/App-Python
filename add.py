import os 
matrix = []

def createUsuario ():

  os.system("clear")
  print('Registro de Contacto')
  print("_________________________________________________________________")
  print("  ")
  name = input('Ingrese los nombres: ')
  print("_________________________________________________________________")
  print("  ")
  surname = input('Ingrese los apellidos: ')
  print("_________________________________________________________________")
  print("  ")
  cc = input('Ingrese la cédula: ')
  print("_________________________________________________________________")
  print("    ")
  gender = (input('Ingrese el genero (M/F): '))
  print("_________________________________________________________________")
  print("    ")
  age = input('Ingrese la fecha de nacimiento (dd-mm-aaaa): ')
  print("_________________________________________________________________")
  print("    ")
  email = input('Ingrese el correo del contacto: ')   
  print("_________________________________________________________________")
  print("    ")
  ciclo = input('Ingrese el cliclo al que pertenece (C1, C2 ó C3): ')   
  print("_________________________________________________________________")
  print("    ")

  name = name.upper()
  surname = surname.upper()
  gender = gender.upper()
  email = email.upper()
  ciclo = ciclo.upper()

  print("contacto validado")
  print(' ')
  print('*******************************************************************')
  print(' ')
  lista = [name, surname, cc, gender, age, email, ciclo]
  matrix.append(lista)
  
  return matrix
