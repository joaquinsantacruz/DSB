![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

Ejercitación 5

Solana

La idea de esta actividad es implementar una solución al mismo enunciado de la

actividad anterior pero su implementación dentro de Solana y sin recurrir a la utilización de

estados en colecciones globales sino al uso de PDAs.

Sistema de Votación con Propuestas

El objetivo de esta ejercitación es desarrollar un contrato inteligente en Anchor que

permita gestionar propuestas y registrar votos de los usuarios de manera segura,

transparente y verificable on-chain.

Requisitos del Sistema

●  Cada propuesta será creada por el administrador del contrato (owner), que será la

cuenta que despliega inicialmente el contrato.

●  Los participantes podrán emitir un único voto por propuesta.

●  El contrato deberá llevar registro de todas las propuestas generadas, la cantidad de

votos que obtiene cada una, y qué cuentas ya han votado.

Garantías del Sistema

El sistema deberá garantizar que:

●  No se puedan votar propuestas inexistentes.

●  Ningún usuario pueda votar dos veces la misma propuesta.

●  Solo el owner pueda crear nuevas propuestas.

●  Toda la información relevante quede almacenada on-chain.

●  El contrato deberá exponer de forma clara y pública los datos de cada propuesta y la

cantidad total de propuestas.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

1- Creación de Propuestas (Solo Owner)

La creación de propuestas sólo puede ser ejecutada por el administrador (owner).

Función Obligatoria:

create\_proposal(title: String) -> Result<u32, Error>

Esta función deberá:

●  Validar que el caller sea el owner.

●  Crear la propuesta con ID incremental.

●  Guardarla en storage.

●  Emitir el evento correspondiente.

2. Votación (Un Solo Voto por Propuesta)

Si un usuario intenta votar nuevamente una misma propuesta, el contrato debe

revertir con el error correspondiente.

Función Obligatoria:

vote(proposal\_id: u32) -> Result<(), Error>

Esta función deberá:

●  Verificar que la propuesta exista.

●  Verificar que el usuario no haya votado antes.

●  Incrementar los votos de la propuesta.

●  Registrar al usuario como “ya votó”.

●  Emitir el evento correspondiente.

3. Funciones de Consulta Pública

Las consultas no pueden modificar el estado del contrato

.Funciones Obligatorias:

get\_proposal(proposal\_id: u32) -> Result<(String, u32), Error>

total\_proposals() -> u32

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

4. Elementos a Guardar en el Contrato

El contrato deberá guardar:

●  Las propuestas

●  La cantidad de votos por propuesta.

●  La lista de usuarios que votaron cada propuesta.

●  El owner del contrato.

6. Desarrollo de Tests en TS (Opcional)

●  Creación de propuestas.

●  Control de acceso para el owner.

●  Registro correcto de votos.

●  Reversión al votar dos veces.

●  Reversión al votar propuestas inexistentes.

![](data:image/png;base64...)