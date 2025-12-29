# Sistema de Gestión de Usuarios con Validación y Almacenamiento en JSON

Este proyecto es una aplicación en Python diseñada para **crear, validar, gestionar y almacenar usuarios** de forma segura y estructurada.  
Incluye un sistema completo de validación de datos, un menú interactivo y almacenamiento persistente en formato **JSON**.

---

## Características principales

### ✔ Validación exhaustiva de datos
El sistema valida cada dato introducido por el usuario:

- Nombre y apellidos  
- Sexo (masculino/femenino)  
- Fecha de nacimiento  
- DNI/NIE con cálculo de letra  
- Teléfono español  
- Email con validación de formato  
- Dirección completa:
  - Calle  
  - Número  
  - Piso  
  - Código postal  
  - Municipio  
  - Ciudad  
  - País  

Cada dato crítico requiere **confirmación explícita** antes de guardarse.

---

## Arquitectura del programa

El proyecto está construido de forma modular:

- **Clase `Usuario`**  
  Representa a cada usuario y facilita la conversión a diccionario para guardarlo en JSON.

- **Funciones de validación**  
  Cada campo tiene su propia función con validación robusta y mensajes claros.

- **Menú interactivo**  
  Permite gestionar usuarios de forma sencilla.

---

##  Funcionalidades del menú

El programa incluye un menú completo:

### 1️ Crear usuario  
Guía paso a paso con validación y confirmación de todos los datos.

### 2️ Buscar usuario  
Permite buscar por DNI/NIE y muestra toda la información del usuario.

### 3️ Listar usuarios  
Muestra todos los usuarios registrados.

### 4 Borrar usuario  
Elimina un usuario por DNI/NIE.

### 5 Guardar y salir  
Guarda todos los usuarios en `usuarios.json` y cierra la aplicación.

---

## Almacenamiento en JSON

Todos los usuarios se guardan en un archivo:
