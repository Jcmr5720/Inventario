import csv
import os


class User:

  def __init__(self, username):
    self.username = username


class Rq:

  def __init__(self, codigo, cant, name):
    self.codigo = codigo
    self.cant = cant
    self.name = name


# Declarar variables
users = [User("adm"), User("user")]
count = 0
rq_list = []  # Array de rqs
check_ref = False
load_data = "N"

# Obtener el usuario
print("INVENTARIO V01\n")
username = input("Bienvenido, por favor digite su usuario: ")
userfound = False
for i in range(len(users)):
  if username == users[i].username:
    userfound = True
    break

  if not userfound:
    print("Acceso denegado")
    exit()
while True:
  load_data_input = input(
    "Los datos de (data.csv) aún no han sido cargados\n¿Deseas cargarlos? (Y/N): "
  )
  if load_data_input.upper() == "Y":
    load_data = True
    break
  elif load_data_input.upper() == "N":
    break
  else:
    print(
      "Respuesta no válida. Por favor, ingrese 'Y' para 'Sí' o 'N' para 'No'.")
if (load_data == True):
  with open("data.csv", "r") as f:
    reader = csv.reader(f)
    count = 0
    check_ref = True
    for row in reader:
      codigo = row[0]
      name = row[1]
      cant = int(row[2])
      count += 1
      rq_inst = Rq(codigo, cant, name)
      rq_list.append(rq_inst)
  print("¡Los datos se han importado a CSV con éxito!")
  print(f"Total de datos cargados: {count}")

# Si el usuario existe, se le da la bienvenida
print("Bienvenido", username)

# Bucle principal
while True:

  # Mostrar el menú principal
  print("""
    ////////////////
    Menu principal
    1. Ingresar referencia al sistema.
    2. Consultar referencia en el sistema.
    3. Mostrar todas las referencias cargadas.
    4. Guardar datos CSV.
    5. Importar datos CSV.
    6. Cerrar sesión.
    """)

  # Obtener la opción del usuario
  opc = input("Digite su opción aqui --> ")
  os.system('cls' if os.name == 'nt' else 'clear')
  # Si la opción es 1, se crea una nueva referencia
  if opc == "1":
    print("""
        ///////
        Ingresar nueva referencia al sistema
        """)
    codigo = input("Ingrese el código de la referencia: ")
    name = input("Ingrese el nombre de la referencia: ")
    cant = int(input("Ingrese la cantidad: "))
    existe_referencia = False
    for i in range(count):
      if codigo == rq_list[i].codigo:
        print("\nEsta referencia ya existe.\n")
        existe_referencia = True
        break
    if not existe_referencia:
      rq_inst = Rq(codigo, cant, name)  # Crear una instancia de la clase rq
      rq_list.append(rq_inst)  # Agregar la instancia a lista rq_list
      count += 1
      check_ref = True

  # Si la opción es 2, se consulta una referencia existente
  elif opc == "2":
    print("""
          ///////
          Consultar referencia
          """)
    codigobuscado = (input("Código referencia: "))
    referencia_encontrada = False
    for i in range(count):
      if (codigobuscado == rq_list[i].codigo):
        print("Nombre:", rq_list[i].name)
        print("Cantidad:", rq_list[i].cant)
        referencia_encontrada = True
        break
    if not referencia_encontrada:
      print("Referencia no válida")

  # Si la opción es 3, se muestran todas las referencias cargadas
  elif opc == "3":

    if (check_ref == False):
      print("\nAún no hay referencias cargadas al sistema.\n")
    if (check_ref == True):
      print("Listado de referencias guardadas")
      print("+------------+------------+------------+")
      print("| Código | Nombre | Cantidad |")
      print("+------------+------------+------------+")
      for i in range(count):
        print(
          f"| {rq_list[i].codigo} | {rq_list[i].name} | {rq_list[i].cant} |"
        )  # Mostrar variables
      print("+------------+------------+------------+")

  # Si la opción es 4, se exporta la data a CSV
  elif opc == "4":
    with open("data.csv", "w") as f:
      writer = csv.writer(f)
      for rq in rq_list:
        writer.writerow([rq.codigo, rq.name, rq.cant])
    print("¡Los datos se han exportado a CSV con éxito!")

    # Si la opción es 5, se importa la data de CSV
  elif opc == "5":
    with open("data.csv", "r") as f:
      reader = csv.reader(f)
      count = 0
      check_ref = True
      for row in reader:
        codigo = row[0]
        name = row[1]
        cant = int(row[2])
        count += 1
        rq_inst = Rq(codigo, cant, name)  # Crear una instancia de la clase rq
        rq_list.append(rq_inst)  # Agregar la instancia a lista rq_list
    print("¡Los datos se han importado a CSV con éxito!")
    print(f"El total de filas en el documento es: {count}")

  # Si la opción es 6, se cierra la sesión
  elif opc == "6":
    print("Sesión cerrada con exito")
    break
  # Si la opción no es válida, se muestra un mensaje de error
  else:
    print("Error -> Opción no valida")
