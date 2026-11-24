![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

Ejercitación 2

Smart Contracts primera parte

1- Libreta de contactos:

Implemente un contrato que permita a cada usuario gestionar su propia libreta de

contactos.

Cada contacto debe tener al menos los siguientes datos: nombre completo, dirección

de Ethereum, teléfono y correo electrónico.

El contrato debe permitir:

- Agregar un nuevo contacto (no se deben permitir duplicados por dirección).

- Consultar los datos de un contacto dado su address.

- Actualizar los datos de un contacto existente.

- Eliminar un contacto.

- Listar todos los contactos registrados por un usuario.

2- Contador Simple

Implemente un contrato que tenga una variable de estado que funcione como

contador.

El contrato debe permitir:

- Incrementar el contador.

- Decrementar el contador.

- Consultar el valor actual del contador.

Las operaciones de lectura y escritura del contador sólo podrán ser realizadas por

un conjunto específico de direcciones, es decir, una whitelist.

La administración de esta whitelist estará a cargo del owner del contrato, definido al

momento del deploy.

Cada vez que el contador sea modificado, se deberá emitir un evento que registre:

- La dirección que realizó la modificación.

- El nuevo valor del contador.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

3- Wallet Personal

Implemente un contrato que permita la gestión de una billetera personal en ether.

El contrato debe permitir:

- Que cualquier usuario pueda depositar fondos en la billetera.

- Que únicamente el propietario (owner) pueda retirar fondos.

- Consultar el balance actual de la billetera.

Se deben emitir eventos que reflejen:

- Cada depósito realizado (con el monto y la dirección que depositó).

- Cada retiro realizado (con el monto y la dirección del owner).

4- Lista de tareas con prioridad

Implemente un contrato que permita a cada usuario manejar su propia lista de tareas

(ToDoList).

Cada tarea debe contener:

- Un id autoincremental.

- Un título (string).

- Una prioridad (entero entre 1 y 5).

- Un estado (pendiente, en curso, completada).

- La fecha/hora de creación (timestamp).

El contrato debe permitir:

- Agregar nuevas tareas.

- Actualizar título, prioridad y estado de una tarea.

- Eliminar tareas.

- Listar todas las tareas de un usuario, con posibilidad de filtrar por prioridad

o estado.

- Implementar paginación en la consulta de tareas, recibiendo parámetros

offset y limit.

Se deben emitir eventos (TaskAdded, TaskUpdated, TaskDeleted,

TaskStatusChanged) para reflejar las operaciones sobre las tareas.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

5- Votación

Implemente un contrato que permita realizar un proceso de votación entre múltiples

candidatos.

El contrato debe permitir:

- Registrar una lista de candidatos disponibles para votar.

- Que los participantes puedan emitir un voto a favor de un único candidato.

- Asegurar que cada participante solo pueda votar una vez.

- Llevar un registro de la cantidad de votos obtenidos por cada candidato.

- Definir una función que permita declarar al ganador, es decir, el candidato

con mayor cantidad de votos.

Se deben emitir eventos para:

- Registrar cada voto realizado.

- Informar el resultado al finalizar la votación.

6- Registro de Usuarios y Muro de Mensajes

Implemente un sistema compuesto por dos contratos inteligentes.

Contrato principal (Registro de Usuarios):

- Permite que cada usuario se registre utilizando su dirección y un nombre de

usuario.

- Lleva un registro único de usuarios para evitar duplicados.

- Expone funciones para consultar si una dirección está registrada y obtener

su nombre de usuario.

Contrato secundario (Muro de Mensajes):

- Permite a los usuarios registrados en el contrato principal publicar mensajes

en un muro público.

- Cada mensaje debe estar asociado al nombre de usuario y la dirección del

remitente.

![](data:image/png;base64...)

x

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

- Solo los usuarios registrados en el contrato principal podrán dejar

mensajes.

- Se debe poder listar todos los mensajes publicados en el muro.

Se deben emitir eventos que reflejen:

- El registro de nuevos usuarios.

- Cada mensaje publicado en el muro.

7- Escrow simple (comprador–vendedor con árbitro)

Implemente un contrato que represente un depósito en garantía (escrow) entre tres

partes:

- Comprador (buyer), Vendedor (seller) y un Árbitro (arbiter).

- El comprador deposita fondos en el contrato. El estado inicial es “Created” y

pasa a “Funded” cuando se reciben fondos.

- El comprador o el árbitro pueden liberar los fondos al vendedor mediante la

función release().

- El vendedor o el árbitro pueden devolver los fondos al comprador mediante

la función refund().

- El contrato debe emitir eventos en cada transición (Funded, Released,

Refunded).

- Validar que no se pueda liberar ni devolver fondos más de una vez, y que

las operaciones respeten los estados definidos.

- Debe implementarse una función view que indique el estado actual del

escrow.

![](data:image/png;base64...)