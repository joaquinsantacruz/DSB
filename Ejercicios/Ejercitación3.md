![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

Ejercitación 3

Web3 py

En esta ejercitación se deberá crear un conjunto de scripts en Python utilizando la librería

Web3.py, que permitan interactuar con los contratos implementados en la Ejercitación 2.

Cada script debe conectarse a la red de pruebas, conectarse al contrato, y realizar las

siguientes operaciones: lectura, escritura y escucha de eventos.

1 - Libreta de Contactos

Requerimientos:

a) Leer: consultar los datos de un contacto por dirección.

b) Escribir: agregar, actualizar y eliminar contactos.

c) Listar todos los contactos del usuario.

d) Escuchar eventos emitidos al agregar, actualizar o eliminar un contacto.

2- Contador Simple

Requerimientos:

a) Leer: obtener el valor actual del contador.

b) Escribir: incrementar y decrementar el contador.

c) Escuchar el evento emitido en cada modificación del contador, mostrando

la dirección que realizó la acción y el nuevo valor.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

3- Wallet Personal

Requerimientos:

a) Leer: consultar el balance actual.

b) Escribir: depositar y retirar fondos (según permisos del owner).

c) Escuchar los eventos de depósito y retiro.

4- Lista de Tareas con Prioridad

Requerimientos:

a) Leer: obtener todas las tareas o filtrarlas por prioridad o estado.

b) Escribir: agregar, actualizar o eliminar tareas.

c) Escuchar eventos de tareas (TaskAdded, TaskUpdated, TaskDeleted,

TaskStatusChanged).

d) Implementar la consulta paginada con parámetros offset y limit.

5- Votación

Requerimientos:

a) Leer: consultar los candidatos y la cantidad de votos.

b) Escribir: emitir un voto por un candidato.

c) Escuchar los eventos de votos registrados y resultado final.

6- Registro de Usuarios y Muro de Mensajes

Requerimientos:

a) Leer: verificar si una dirección está registrada y obtener su nombre.

b) Escribir: registrar usuarios y publicar mensajes.

c) Escuchar los eventos de nuevo registro y mensajes publicados.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

7- Escrow Simple (Comprador–Vendedor con Árbitro)

Requerimientos:

a) Leer: consultar el estado actual del escrow.

b) Escribir: depositar fondos, liberar o reembolsar según roles y estado.

c) Escuchar los eventos Funded, Released y Refunded.

Nota:

Cada script debe implementar la conexión con el contrato mediante su ABI y dirección

desplegada.

Se recomienda estructurar las funciones en Python de manera modular (por ejemplo:

get\_balance(), add\_contact(), vote\_candidate(), etc.) y probar todas las funciones públicas

definidas en cada contrato.

![](data:image/png;base64...)