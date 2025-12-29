print("Bienvenidos al programa para crear usuarios.\n")

from datetime import datetime
import json

# ============================
# CLASE USUARIO
# ============================

class Usuario:
    def __init__(self, nombre, apellidos, sexo, fecha_nacimiento,
                 documento, telefono, email, pais,
                 calle, numero, piso, codigo_postal, municipio, ciudad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.documento = documento
        self.telefono = telefono
        self.email = email
        self.pais = pais
        self.calle = calle
        self.numero = numero
        self.piso = piso
        self.codigo_postal = codigo_postal
        self.municipio = municipio
        self.ciudad = ciudad

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "sexo": self.sexo,
            "fecha_nacimiento": self.fecha_nacimiento.strftime('%d/%m/%Y'),
            "documento": self.documento,
            "telefono": self.telefono,
            "email": self.email,
            "pais": self.pais,
            "direccion": {
                "calle": self.calle,
                "numero": self.numero,
                "piso": self.piso,
                "codigo_postal": self.codigo_postal,
                "municipio": self.municipio,
                "ciudad": self.ciudad
            }
        }

# ============================
# FUNCIONES DE VALIDACIÓN BASE
# ============================

def pedir_entero_en_rango(mensaje, minimo, maximo, intentos=3):
    for intento in range(1, intentos + 1):
        try:
            valor = int(input(mensaje))
            if valor < minimo or valor > maximo:
                raise ValueError()
            return valor
        except ValueError:
            print(f"Error: solo se admiten valores numéricos dentro del rango permitido. Intento {intento}/{intentos}")
    print("Has superado el número máximo de intentos. Cerrando el programa...")
    exit()

def pedir_fecha_valida(intentos=3):
    for intento in range(1, intentos + 1):
        dia = pedir_entero_en_rango("Introduce el día de nacimiento: ", 1, 31)
        mes = pedir_entero_en_rango("Introduce el mes de nacimiento: ", 1, 12)
        anio = pedir_entero_en_rango("Introduce el año de nacimiento: ", 1900, 2025)
        try:
            fecha = datetime(anio, mes, dia)
            return fecha
        except ValueError:
            print(f"Error: la fecha {dia}/{mes}/{anio} no es válida. Intento {intento}/{intentos}")
    print("Fecha incorrecta. Has superado los intentos.")
    exit()

def confirmar_fecha(fecha, intentos=3):
    for intento in range(1, intentos + 1):
        respuesta = input(f"Tu fecha de nacimiento es: {fecha.strftime('%d/%m/%Y')}. ¿Es correcta? (si/no): ").strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print(f"Error: responde solo 'si' o 'no'. Intento {intento}/{intentos}")
    print("Fecha incorrecta. Has superado los intentos.")
    exit()

def pedir_texto_solo_letras(mensaje, intentos=3):
    for intento in range(1, intentos + 1):
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto.lower()
        print(f"Error: solo se admiten letras. Intento {intento}/{intentos}")
    print("Has superado el número máximo de intentos. Cerrando el programa...")
    exit()

def confirmar_dato(nombre_dato, valor, intentos=3):
    for intento in range(1, intentos + 1):
        resp = input(f"Has introducido el {nombre_dato}: {valor}. ¿Es correcto? (si/no): ").strip().lower()
        if resp == "si":
            return True
        elif resp == "no":
            return False
        else:
            print(f"Error: responde solo 'si' o 'no'. Intento {intento}/{intentos}")
    print(f"{nombre_dato.capitalize()} incorrecto. Has superado los intentos.")
    exit()

# ============================
# NOMBRE, SEXO Y DOCUMENTACIÓN
# ============================

def pedir_nombre_completo(intentos=3):
    for intento in range(1, intentos + 1):
        nombre = pedir_texto_solo_letras("Introduce tu nombre: ")
        apellidos = pedir_texto_solo_letras("Introduce tus apellidos: ")
        nombre_completo = f"{nombre} {apellidos}"
        print(f"\nHas introducido: {nombre_completo}")
        confirmacion = input("¿Es correcto? (si/no): ").strip().lower()
        if confirmacion == "si":
            return nombre, apellidos
        elif confirmacion == "no":
            print(f"Vamos a repetir los datos. Intento {intento}/{intentos}\n")
        else:
            print(f"Error: responde solo 'si' o 'no'. Intento {intento}/{intentos}\n")
    print("Nombre o apellidos incorrectos. Has superado los intentos.")
    exit()

def pedir_sexo(intentos=3):
    for intento in range(1, intentos + 1):
        sexo = input("Introduce tu sexo (masculino/femenino): ").strip().lower()
        if sexo in ["masculino", "femenino"]:
            if confirmar_dato("sexo", sexo):
                return sexo
            else:
                print(f"Vamos a repetir el sexo. Intento {intento}/{intentos}\n")
                continue
        print(f"Error: debes escribir 'masculino' o 'femenino'. Intento {intento}/{intentos}")
    print("Sexo incorrecto. Has superado los intentos.")
    exit()

def pedir_dni_o_nie(intentos=3):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    prefijos_nie = {"x": "0", "y": "1", "z": "2"}

    for intento in range(1, intentos + 1):
        doc = input("Introduce tu DNI o NIE: ").strip().lower()

        # DNI
        if len(doc) == 9 and doc[:-1].isdigit() and doc[-1].isalpha():
            numero = int(doc[:-1])
            letra_correcta = letras[numero % 23].lower()
            if doc[-1] == letra_correcta:
                if confirmar_dato("documento", doc):
                    return doc
                continue

        # NIE
        if len(doc) == 9 and doc[0] in prefijos_nie and doc[1:8].isdigit() and doc[-1].isalpha():
            numero_convertido = prefijos_nie[doc[0]] + doc[1:8]
            numero = int(numero_convertido)
            letra_correcta = letras[numero % 23].lower()
            if doc[-1] == letra_correcta:
                if confirmar_dato("documento", doc):
                    return doc
                continue

        print(f"Error: documento inválido. Ejemplos válidos: 12345678z, x1234567l. Intento {intento}/{intentos}")

    print("Documento incorrecto. Has superado los intentos.")
    exit()

# ============================
# TELÉFONO Y EMAIL
# ============================

def pedir_telefono(intentos=3):
    for intento in range(1, intentos + 1):
        telefono = input("Introduce tu número de teléfono: ").strip()
        if telefono.isdigit() and len(telefono) == 9 and telefono[0] in "6789":
            if confirmar_dato("teléfono", telefono):
                return telefono
            continue
        print(f"Error: el teléfono debe tener 9 dígitos y empezar por 6, 7, 8 o 9. Intento {intento}/{intentos}")
    print("Teléfono incorrecto. Has superado los intentos.")
    exit()

def email_valido(email: str) -> bool:
    if " " in email:
        return False
    if "@" not in email:
        return False
    parte_local, _, dominio = email.partition("@")
    if not parte_local or not dominio:
        return False
    if "." not in dominio:
        return False
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    return True

def pedir_email(intentos=3):
    for intento in range(1, intentos + 1):
        email = input("Introduce tu email: ").strip().lower()
        if email_valido(email):
            if confirmar_dato("email", email):
                return email
            else:
                print(f"Vamos a repetir el email. Intento {intento}/{intentos}\n")
                continue
        print(f"Error: el email no tiene un formato válido. Intento {intento}/{intentos}")
    print("Email incorrecto. Has superado los intentos.")
    exit()

# ============================
# DIRECCIÓN COMPLETA
# ============================

def pedir_calle(intentos=3):
    for intento in range(1, intentos + 1):
        calle = input("Introduce tu calle: ").strip().lower()
        if calle.replace(" ", "").isalpha():
            return calle
        print(f"Error: la calle solo puede contener letras. Intento {intento}/{intentos}")
    print("Calle incorrecta. Has superado los intentos.")
    exit()

def pedir_numero(intentos=3):
    for intento in range(1, intentos + 1):
        numero = input("Introduce el número de la vivienda: ").strip()
        if numero.isdigit():
            return numero
        print(f"Error: el número debe ser numérico. Intento {intento}/{intentos}")
    print("Número incorrecto. Has superado los intentos.")
    exit()

def pedir_piso(intentos=3):
    for intento in range(1, intentos + 1):
        piso = input("Introduce el piso (si no tienes, escribe '0'): ").strip().lower()
        if piso.replace(" ", "").isalnum():
            return piso
        print(f"Error: el piso solo puede contener letras, números y espacios. Intento {intento}/{intentos}")
    print("Piso incorrecto. Has superado los intentos.")
    exit()

def confirmar_direccion(calle, numero, piso, intentos=3):
    direccion = f"{calle} {numero}, piso {piso}"
    for intento in range(1, intentos + 1):
        resp = input(f"Tu dirección es: {direccion}. ¿Es correcta? (si/no): ").strip().lower()
        if resp == "si":
            return True
        elif resp == "no":
            return False
        else:
            print(f"Error: responde solo 'si' o 'no'. Intento {intento}/{intentos}")
    print("Dirección incorrecta. Has superado los intentos.")
    exit()

def pedir_codigo_postal(intentos=3):
    for intento in range(1, intentos + 1):
        cp = input("Introduce tu código postal (5 dígitos): ").strip()
        if cp.isdigit() and len(cp) == 5:
            if confirmar_dato("código postal", cp):
                return cp
            continue
        print(f"Error: el código postal debe tener 5 dígitos. Intento {intento}/{intentos}")
    print("Código postal incorrecto. Has superado los intentos.")
    exit()

def pedir_municipio(intentos=3):
    for intento in range(1, intentos + 1):
        municipio = input("Introduce tu municipio de residencia: ").strip().lower()
        if municipio.replace(" ", "").isalpha():
            if confirmar_dato("municipio", municipio):
                return municipio
            continue
        print(f"Error: el municipio solo puede contener letras. Intento {intento}/{intentos}")
    print("Municipio incorrecto. Has superado los intentos.")
    exit()

def pedir_ciudad(intentos=3):
    for intento in range(1, intentos + 1):
        ciudad = input("Introduce tu ciudad de residencia: ").strip().lower()
        if ciudad.replace(" ", "").isalpha():
            if confirmar_dato("ciudad", ciudad):
                return ciudad
            continue
        print(f"Error: la ciudad solo puede contener letras. Intento {intento}/{intentos}")
    print("Ciudad incorrecta. Has superado los intentos.")
    exit()

def pedir_pais(intentos=3):
    for intento in range(1, intentos + 1):
        pais = input("Introduce tu país de residencia: ").strip().lower()
        if pais.replace(" ", "").isalpha():
            if confirmar_dato("país", pais):
                return pais
            continue
        print(f"Error: el país solo puede contener letras. Intento {intento}/{intentos}")
    print("País incorrecto. Has superado los intentos.")
    exit()

# ============================
# CREACIÓN DE UN USUARIO
# ============================

def crear_usuario():
    # Fecha de nacimiento
    for intento in range(1, 4):
        fecha_nacimiento = pedir_fecha_valida()
        if confirmar_fecha(fecha_nacimiento):
            print(f"Fecha confirmada: {fecha_nacimiento.strftime('%d/%m/%Y')}\n")
            break
        else:
            print(f"La fecha no es correcta. Intento {intento}/3\n")
    else:
        exit()

    # Nombre y sexo
    nombre, apellidos = pedir_nombre_completo()
    print(f"Nombre confirmado: {nombre} {apellidos}\n")

    sexo = pedir_sexo()
    print(f"Sexo confirmado: {sexo}\n")

    # Documento
    documento = pedir_dni_o_nie()
    print(f"Documento confirmado: {documento}\n")

    # Teléfono
    telefono = pedir_telefono()
    print(f"Teléfono confirmado: {telefono}\n")

    # Email
    email = pedir_email()
    print(f"Email confirmado: {email}\n")

    # Dirección
    while True:
        calle = pedir_calle()
        numero = pedir_numero()
        piso = pedir_piso()

        if confirmar_direccion(calle, numero, piso):
            print(f"Dirección confirmada: {calle} {numero}, piso {piso}\n")
            break
        else:
            print("Vamos a repetir la dirección completa.\n")

    codigo_postal = pedir_codigo_postal()
    print(f"Código postal confirmado: {codigo_postal}\n")

    municipio = pedir_municipio()
    print(f"Municipio confirmado: {municipio}\n")

    ciudad = pedir_ciudad()
    print(f"Ciudad confirmada: {ciudad}\n")

    pais = pedir_pais()
    print(f"País confirmado: {pais}\n")

    # Crear instancia de Usuario
    usuario = Usuario(
        nombre=nombre,
        apellidos=apellidos,
        sexo=sexo,
        fecha_nacimiento=fecha_nacimiento,
        documento=documento,
        telefono=telefono,
        email=email,
        pais=pais,
        calle=calle,
        numero=numero,
        piso=piso,
        codigo_postal=codigo_postal,
        municipio=municipio,
        ciudad=ciudad
    )

    # Resumen final
    print("\n=== USUARIO CREADO CORRECTAMENTE ===")
    print(f"Nombre completo: {usuario.nombre} {usuario.apellidos}")
    print(f"Sexo: {usuario.sexo}")
    print(f"Fecha de nacimiento: {usuario.fecha_nacimiento.strftime('%d/%m/%Y')}")
    print(f"Documento: {usuario.documento}")
    print(f"Teléfono: {usuario.telefono}")
    print(f"Email: {usuario.email}")
    print(f"Dirección: {usuario.calle} {usuario.numero}, piso {usuario.piso}")
    print(f"Código postal: {usuario.codigo_postal}")
    print(f"Municipio: {usuario.municipio}")
    print(f"Ciudad: {usuario.ciudad}")
    print(f"País: {usuario.pais}")
    print("====================================\n")

    return usuario

# ============================
# PROGRAMA PRINCIPAL (VARIOS USUARIOS)
# ============================

usuarios = []

while True:
    usuario = crear_usuario()
    usuarios.append(usuario.a_diccionario())

    continuar = input("¿Quieres crear otro usuario? (si/no): ").strip().lower()
    if continuar != "si":
        break
    print("\nVamos a crear otro usuario...\n")

# Guardar todos los usuarios en un solo JSON
nombre_archivo = "usuarios.json"
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

print(f"\nSe han almacenado {len(usuarios)} usuario(s) en el archivo '{nombre_archivo}'.")