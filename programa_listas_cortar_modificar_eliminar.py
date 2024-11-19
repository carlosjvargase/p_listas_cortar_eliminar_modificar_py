'''
Escriba un programa que permita crear una lista de palabras y que, a continuación de 5 opciones:

1. Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista.
2. Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
3. Eliminar: Me pide una cadena, y la elimina de la lista.
4. Mostrar: Muestra la lista de cadenas.
5. Terminar.
'''
def menu():
  print('''
###### Menú #####
1. Contar.
2. Modificar.
3. Eliminar.
4. Mostrar.
5. Terminar.
  ''')
  return input('Selecciona una opción: ')

lista_cadenas = []
while True:
  palabra = input('Ingresa una palabra (* para salir): ').lower()
  if palabra == '*': break
  lista_cadenas.append(palabra)
while True:
  opc = menu()
  if opc == '1':
    palb = input('Ingresa la palabra a contar: ')
    print(f'La palabra {palb} está {lista_cadenas.count(palb)} veces')
  elif opc == '2':
    pal_ori   = input('Ingresa la palabra a modificar: ')
    pal_reemp = input('Ingresa la palabra de reemplazo: ')
    if pal_ori in lista_cadenas:
      for x in range(len(lista_cadenas)):
        if lista_cadenas[x] == pal_ori:
          lista_cadenas[x] = pal_reemp
      print('Palabra reemplazada.')
    else:
      print('Palabra a modificar no se encuentra en el listado.')
  elif opc == '3':
    palb = input('Ingresa la palabra a eliminar: ')
    if palb in lista_cadenas:
      n_veces = lista_cadenas.count(palb)
      for j in range(n_veces):
        lista_cadenas.remove(palb)
      print('Palabra eliminada.')
    else:
      print('Palabra a eliminar no se encuentra en el listado.')
  elif opc == '4':
    print(lista_cadenas)
  elif opc == '5':
    print('Muchas gracias por usar nuestra aplicación.')
    break
  else:
    print('Opción no válida')