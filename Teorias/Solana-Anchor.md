![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

![](data:image/png;base64...)

Conceptos

● Solana

○ Origen

○ Algoritmo de consenso

○ Cuentas

○ Algoritmo de hash y curva elíptica

○ Anchor

![](data:image/png;base64...)

Solana: origen

● 2017: Anatoly Yakovenko (ex‑Qualcomm, sistemas distribuidos de alta performance)

publica el primer borrador de Proof of History.

● 2018: se funda Solana Labs(empresa que creó y desarrolla el software principal de

Solana) junto con Raj Gokal, Greg Fitzgerald, Stephen Akridge.

● 2020: se lanza la mainnet beta de Solana.

https://solana.com/solana-whitepaper.pdf

![](data:image/png;base64...)

Solana: origen -> contexto

❖ Trilema: seguridad vs descentralización vs performance.

❖ Limitaciones de L1 tradicionales:

➢ Bitcoin: muy seguro pero tps muy bajo.

➢ Ethereum L1: más ﬂexible (EVM) pero también limitado en TPS y fees altos en

congestión.

Visión de Solana:

➢ Un L1 monolítico de altísimo rendimiento, sin sharding ni L2, con un solo estado global y

tiempo de bloque ~400 ms.

![](data:image/png;base64...)

Arquitectura

● Proof of History (PoH): reloj criptográﬁco (VDF) que ordena eventos.

● Tower BFT: consenso PBFT‑like basado en PoS, usando PoH como reloj.

● Gulf Stream: forwarding de transacciones sin mempool global.

● Turbine: protocolo de propagación de bloques tipo "BitTorrent".

● Sealevel: runtime paralelo que ejecuta muchas transacciones/programas a

la vez.

![](data:image/png;base64...)

Arquitectura: PoH

Problema: en redes distribuidas, todos necesitan ponerse de acuerdo

en el orden de las transacciones.

PoH crea una secuencia veriﬁcable de hashes que actúa como "reloj

común".

Cada hash ("tick") demuestra que pasó tiempo desde el anterior,

porque hay que ejecutar SHA‑256 muchas veces en secuencia.

![](data:image/png;base64...)

Arquitectura: PoH

El líder(un validador seleccionado) recibe las transacciones, pero NO elige arbitrariamente el orden

Cuando llega una transacción, el líder la inyecta en la secuencia:

h101 = SHA256(h100 || tx\_A)

h102 = SHA256(h101 || tx\_B)

Esto signiﬁca:

La transacción queda ordenada por la posición en la secuencia PoH.

Una vez mezclada en PoH, su orden queda sellado criptográﬁcamente.

Cualquier nodo puede veriﬁcar ese orden sin conﬁar en el líder.

![](data:image/png;base64...)

Arquitectura: PoH

🟥 Ethereum

El validador decide el orden.

Puede ordenar tx según gas, MEV, preferencia propia.

🟩 Solana

PoH decide el orden.

El líder no puede reordenar sin romper la secuencia hash.

No hay mempool.

No hay reordenamiento por el validador.

No hay timestamp manual.

Solo tiempo criptográﬁco secuencial.

![](data:image/png;base64...)

Arquitectura: PoH

En Solana, el orden de las transacciones no lo elige el validador: lo impone el reloj criptográﬁco de Proof of

History al insertar cada transacción en la secuencia de hashes.

El líder es un validador al que le toca, durante un período muy corto (un slot de ~400 ms), la tarea de:

Recibir transacciones.

● Insertarlas en la secuencia PoH.

● Ejecutarlas.

● Producir el bloque de ese slot.

● Propagar ese bloque al resto de la red.

Entonces el orden queda “grabado” exactamente en el momento en que la tx llegó al líder

![](data:image/png;base64...)

Arquitectura: Qué es un slot?

Un slot es una unidad ﬁja de tiempo en Solana durante la cual un validador especíﬁco (el líder)

tiene el derecho y la responsabilidad de producir un bloque.

Es el “turno” del líder.

Duración aproximada

Un slot dura ~400 ms.

Es decir: ~2.5 slots por segundo.

(La duración exacta puede variar levemente según optimizaciones del cliente del validador.)

Un slot es el intervalo de tiempo en el que un líder debe ejecutar PoH, recibir transacciones y

construir un bloque.

![](data:image/png;base64...)

Arquitectura: Qué es un epoch?

Un epoch es un período de tiempo compuesto por una gran cantidad de slots (aprox. 432.000 slots), durante el cual:

● Se ﬁja el leader schedule (quién es líder en cada slot).

● Se ajustan las recompensas de staking.

● Se recalculan los stakes efectivos.

● Se actualizan ciertos parámetros de la red.

Cada slot dura ~400 ms.

Un epoch tiene unos 432.000 slots.

Duración aproximada: 1.5 a 2 días, dependiendo de las variaciones en el ritmo de slots.

![](data:image/png;base64...)

Arquitectura: Qué es un epoch?

Dentro de ese epoch:

● Ya está deﬁnido quién producirá cada bloque.

● Ya se sabe qué stake tiene cada validador.

● Las recompensas se acumulan y se pagan al ﬁnal del epoch siguiente.

● La delegación de stake solo se activa completamente en el próximo

epoch.

![](data:image/png;base64...)

Arquitectura: Tower BFT

Tower BFT es un algoritmo donde los validadores votan secuencialmente sobre bloques y cada voto amplía un

período obligatorio (lockout) que les impide cambiar de rama.

Cuando suﬁcientes validadores acumulan lockouts sobre una misma cadena, esa cadena se vuelve irreversible

(ﬁnalized).

Un voto es un mensaje ﬁrmado por un validador que dice: “El bloque del slot X es parte de la cadena válida que

estoy siguiendo”

Ese voto incluye:

● Slot votado

● Parent slot (referencia al bloque anterior)

● Lockout asociado

● Firma del validador

El voto se reﬁere SIEMPRE a un slot, no a un bloque completo.

Esto es importante porque los slots pueden estar vacíos, pero igual mantienen estructura temporal.

![](data:image/png;base64...)

Arquitectura: Tower BFT

¿Qué es un lockout realmente?

Un lockout NO es solamente tiempo bloqueado

Es un período en el cual el validador está obligado a NO votar en un fork diferente, porque romperlo implica:

● perder recompensas acumuladas,

● invalidar sus votos previos,

● reducir su credibilidad,

● afectar el schedule futuro,

● afectar a sus delegadores.

El lockout se mide en slots, no en segundos.

![](data:image/png;base64...)

Arquitectura: Tower BFT

Ejemplo:

Voto al slot 100 → lockout = 2 slots

Siguiente voto → lockout = 2×2 = 4

Siguiente voto → lockout = 4×2 = 8

Siguiente voto → lockout = 8×2 = 16

El lockout del último voto afecta a TODOS los votos anteriores.

![](data:image/png;base64...)

Arquitectura: Tower BFT

Cada vez que un validador vota, el lockout del voto anterior se duplica.

Esto crea un efecto:

○ Al principio, es fácil cambiar de rama - Lockout pequeño (2 slots)

○ Después de varios votos seguidos, cambiar de rama es muy costoso -Lockout grande (256, 512, 1024 slots)

○ suﬁcientes validadores acumulando lockouts grandes

No hace falta comunicación extra.

El simple acto de votar crea el compromiso.

Tower BFT reemplaza las rondas de consenso tradicionales por un sistema de votos encadenados con lockouts

exponenciales.

Cada voto obliga al validador a mantenerse en la misma rama, y romper un lockout implica pérdidas económicas.

Así, la red converge rápidamente en una única cadena, y PoH le da a Tower un reloj global que elimina retardos.

![](data:image/png;base64...)

Arquitectura: Qué es Gulf Stream?

Gulf Stream es el protocolo de Solana que elimina el mempool tradicional y envía las transacciones directamente al

futuro líder del slot antes de que su turno llegue.

Es decir:

No hay un “mempool global” como en Ethereum.

Las transacciones no quedan dando vueltas en la red esperando un minero.

Cada transacción se encamina directamente hacia el validador que será líder en el slot donde probablemente se

procese.

Esto es posible porque Solana tiene un leader schedule determinístico:

todos saben quién será líder en el futuro.

![](data:image/png;base64...)

Arquitectura: ¿Qué hace Gulf Stream exactamente?

Envía las transacciones directo al validador que será líder

Ejemplo:

Slot 100 → líder será Validador A

Slot 101 → líder será Validador B

Slot 102 → líder será Validador C

Cuando un usuario envía una tx, la red la encamina a:

A si se espera que se procese en slot 100,

B si va a procesarse en slot 101,

C si es para slot 102.

Esto es lo que se llama forwarding.

![](data:image/png;base64...)

Arquitectura: ¿Qué hace Gulf Stream exactamente?

Garantiza que Solana pueda procesar miles de transacciones por segundo

Si el líder tuviera que esperar a recibir las transacciones dentro del mismo slot, no lo lograría:

● un slot dura solo ~400 ms,

● las tx tardan en propagarse por la red,

● sería imposible ejecutar tanto en tan poco tiempo.

★ Gulf Stream pre-carga el trabajo.

★ Reduce la latencia y acelera la red

★ Una tx puede conﬁrmarse en <<1 segundo.

Permite manejo eﬁciente de congestión

★ Si la red está saturada → las tx se enrutan solo a líderes relevantes, no a todos los nodos.

![](data:image/png;base64...)

Arquitectura: ¿Qué pasa si el líder se cae?

Supongamos que el líder de slot 100 falla.

Las transacciones ya fueron enviadas también al líder del slot 101.

El líder 101 puede procesarlas inmediatamente.

La red no se congela ni pierde tx.

Esto mejora la resiliencia frente a fallas.

![](data:image/png;base64...)

Arquitectura: Turbine

Turbine es el protocolo de Solana para distribuir bloques y datos a la red usando un modelo tipo BitTorrent: divide el

bloque en paquetes y los reparte en forma de árbol hacia los validadores.

Es el componente que permite que:

Un bloque producido en ~400 ms

Se difunda a toda la red

Sin colapsarla con tráﬁco

Y sin que el líder tenga que enviarlo a todos

Es el equivalente a cómo funcionan los torrents: el líder envía fragmentos, y los validadores ayudan a retransmitir.

![](data:image/png;base64...)

Arquitectura: Turbine

En redes como Bitcoin o Ethereum:

El minero/líder debe enviar el bloque completo a cientos de nodos.

Esto genera latencias enormes.

Aumenta la probabilidad de forks.

Congestiona nodos con poca capacidad de red.

En Solana, esto sería imposible:

no podés mandar un bloque entero de 1 MB a miles de nodos en 400 ms.

Turbine resuelve este cuello de botella.

![](data:image/png;base64...)

Arquitectura: Turbine funcionamiento

El líder divide el bloque en “shreds” (fragmentos)

Un bloque se divide en pequeños paquetes:

1 shred ≈ 1–2 KB

Un bloque tiene cientos o miles de shreds

Cada shred está autenticado con PoH y Merkle-like structures

Ejemplo:

Bloque = 600 KB

Shreds = 300 fragmentos de 2 KB

![](data:image/png;base64...)

Arquitectura: Turbine funcionamiento

El líder NO envía todos los shreds a todos

Esto sería imposible.

En vez de eso, Solana crea un árbol de re-transmisión.

Ejemplo simpliﬁcado:

Líder

├── Nodo A

├── Nodo B

└── Nodo C

El líder envía solo parte de los shreds a cada uno.

![](data:image/png;base64...)

Arquitectura: Turbine funcionamiento

Cada nodo “hoja” reenvía parte del paquete a otros nodos

Ejemplo:

Líder → A recibe shreds 1–100

Líder → B recibe shreds 101–200

Líder → C recibe shreds 201–300

Luego:

A → envía parte de sus shreds a otros validadores del subárbol A

B → envía los suyos a subárbol B

C → envía los suyos a subárbol C

Cada validador solo transmite a unos pocos nodos, no a todos.

![](data:image/png;base64...)

Arquitectura: Turbine: conclusión

❖ No todos reciben todo directamente del líder: el líder no se satura.

❖ Cada validador solo reenvía lo que le corresponde: menos ancho de banda por

nodo.

❖ El árbol permite que el bloque llegue a TODOS los nodos: distribución eﬁciente.

❖ Los shreds están ﬁrmados y veriﬁcables: si un nodo recibe datos corruptos, sabe

que están mal.

❖ Resiliencia ante fallas: aunque un nodo intermedio falle, otros subárboles siguen

propagando.

![](data:image/png;base64...)

Arquitectura: Sealevel

Es el runtime de Solana capaz de ejecutar miles de transacciones en paralelo, siempre

que no compitan por las mismas cuentas.

Ethereum: 1 transacción por vez (secuencial).

Solana: muchas transacciones al mismo tiempo (paralelo).

Sealevel es lo que permite que Solana alcance decenas de miles de TPS.

En Ethereum:

● Cada transacción puede tocar cualquier estado.

● No se sabe qué cuentas toca hasta ejecutar el código.

● No se puede paralelizar sin riesgo de race conditions.

![](data:image/png;base64...)

Arquitectura: Sealevel

Por eso:

La EVM ejecuta las transacciones una por una, secuencialmente.

En Solana:

Cada transacción declara explícitamente qué cuentas va a leer y qué cuentas va a

escribir ANTES de ejecutarse.

Eso permite paralelizar.

![](data:image/png;base64...)

Arquitectura: Sealevel

la arquitectura clave: Account List (lista de cuentas)

Cada transacción trae:

● Lista de cuentas read-only

● Lista de cuentas writable

● Flags como “signer” o “PDA”

Ejemplo:

Como no comparten cuentas → Sealevel las ejecuta en

paralelo

![](data:image/png;base64...)

Arquitectura: Sealevel

Sealevel detecta conﬂictos automáticamente

Ejemplo de conﬂicto:

→ No se pueden ejecutar juntas.

![](data:image/png;base64...)

Arquitectura: Sealevel

Sealevel puede identiﬁcar que distintas transacciones llaman al MISMO programa, al

MISMO método, pero sobre cuentas diferentes.

Qué pasa si dos transacciones compiten por la misma cuenta?

serializa solo esas dos, deja que todas las demás vayan en paralelo.

Ejemplo:

![](data:image/png;base64...)

Cuentas- storage

Solana NO tiene un “estado global” como Ethereum.

Solana usa cuentas independientes, cada una con su propio dueño, datos, lamports y permisos.

El runtime nunca lee o escribe memoria global.

Todo estado está contenido en accounts.

Esto es lo que hace posible:

● Ejecución paralela (Sealevel)

● Aislamiento de estado

● Evitar race conditions

● Validación estática de conﬂictos

● Programas más seguros

● Storage descentralizado y granular

![](data:image/png;base64...)

Cuentas- Storage

Todos los datos en la red Solana se almacenan en cuentas. Puedes pensar en la red Solana como

una base de datos pública con una única tabla de Cuentas. La relación entre una cuenta y su

dirección es similar a la de un par clave-valor (key-value), donde la clave es la dirección y el valor es

la cuenta.

Cada cuenta tiene la misma estructura básica y puede ser localizada usando su dirección.

![](data:image/png;base64...)

Cuentas- Storage

Una account es la unidad básica de almacenamiento del estado en Solana.

Cada cuenta contiene:

● Pubkey (la dirección de la cuenta): 32 bytes en base58 → identiﬁcador único

● Lamports: El saldo de SOL que posee la cuenta — también sirve para pagar rent.

● Owner (program\_id): El programa que tiene permiso para modiﬁcar esta cuenta. (Solo el

owner puede cambiar el campo data o descontar lamports)

● Data: Los bytes que representan el estado interno de la cuenta. Hasta 10 MB máximo (muy

generoso para una blockchain L1).

● Executable (boolean): Indica si esta cuenta contiene código BPF (es un programa).

![](data:image/png;base64...)

Cuentas- Storage

![](data:image/png;base64...)

Cuentas- Storage: Tipos de cuentas en Solana

● System Accounts: Wallets, fee payers, cuentas básicas creadas por System Program.

● Program Accounts: Cuentas cuyo campo executable = true, (contienen código BPF compilado

desde Rust/C/C++. La lógica del smart contract)

![](data:image/png;base64...)

Cuentas- Storage: Tipos de cuentas en Solana

● Data Accounts: Cuentas donde un programa

guarda su estado interno.

■ SPL Token Accounts: Cuentas especializadas

creadas por el Token Program.

![](data:image/png;base64...)

Cuentas- Storage: Tipos de cuentas en Solana

¿Qué es una cuenta ejecutable?

Cuando se despliega un programa:

Su código se sube a una cuenta especial y se marca como executable = true

El owner pasa a ser BPF Loader Program

Esa cuenta no tiene datos mutables (solo código)

No se puede escribir salvo durante el deployment/upgrade autorizado

![](data:image/png;base64...)

Cuentas- Storage: Tipos de cuentas en Solana

Cómo funciona el almacenamiento?

El estado se guarda dentro de la cuenta, no dentro del programa.

Ejemplo de cuenta de usuario:

struct UserProﬁle {

authority: Pubkey,

counter: u64,

nickname: [u8; 32],

}

Esto se serializa y se guarda en la sección data de la cuenta asociada.

![](data:image/png;base64...)

Cuentas- Storage: Rent y REMT

Rent es el mecanismo mediante el cual Solana requiere que toda cuenta tenga una cantidad

mínima de SOL para justiﬁcar el espacio de almacenamiento que ocupa en la red.

Solana replica cada cuenta en todos los validadores, por lo que almacenar información tiene un

costo real.

El rent sirve para evitar:

acumulación de cuentas basura,

ataques que llenen el storage,

consumo ilimitado de espacio on-chain.

Si una cuenta no tiene suﬁciente SOL, puede ser marcada como “infrarrent” y potencialmente

eliminada para recuperar espacio.

![](data:image/png;base64...)

Cuentas- Storage: Rent y REMT

REMT (Rent-Exempt Minimum Threshold)

REMT es la cantidad mínima de SOL que una cuenta debe tener para ser considerada “rent-exempt”,

es decir, exenta de pagar rent y protegida contra eliminación.

REMT depende exclusivamente del tamaño en bytes de la cuenta.

Mientras tenga ese mínimo:

NO paga rent,

NO será recolectada,

Puede existir indeﬁnidamente,

Funciona como un depósito reembolsable (si cerrás la cuenta, recuperás el SOL).

![](data:image/png;base64...)

Función de hash y curva elíptica

Solana usa SHA-256 como función hash principal en dos lugares esenciales del protocolo:

A) En el Proof of History

PoH es básicamente una cadena secuencial de hashes SHA-256:

h₀ = seed inicial

h₁ = SHA256(h₀)

h₂ = SHA256(h₁)

h₃ = SHA256(h₂)

Esta secuencialidad crea un reloj criptográﬁco, inmutable, veriﬁcable por cualquier nodo, imposible

de paralelizar.

Por eso PoH funciona como un VDF (Veriﬁable Delay Function).

![](data:image/png;base64...)

Función de hash

B) En otras estructuras internas

SHA-256 también se usa para:

derivar PDAs (Program Derived Addresses)

ﬁrmar mensajes intermedios

generar seeds internos

hashes de bloques/ticks

![](data:image/png;base64...)

Curva elíptica

Solana usa Ed25519, una curva elíptica moderna, rápida y muy segura basada en:

la curva Curve25519,

el esquema de ﬁrma EdDSA,

claves de 32 bytes,

ﬁrmas de 64 bytes,

alta resistencia a ataques de canal lateral.

![](data:image/png;base64...)

Curva elíptica

![](data:image/png;base64...)

¿Qué es una PDA?

Una PDA(Program Derived Address) es una dirección de cuenta generada de manera determinística

por un programa, sin una clave privada asociada, y que solo ese programa puede “ﬁrmar” mediante

seeds.

En otras palabras:

● No la controla un usuario

● No hay private key

● No puede usarse desde una wallet

● Nadie la puede tomar

● Solo el programa dueño puede modiﬁcarla

● Sirve para guardar estado seguro del programa

![](data:image/png;base64...)

¿Por qué Solana necesita PDAs?

Porque los programas necesitan:

cuentas “propias” para guardar estado,

vaults de tokens,

conﬁguración global,

perﬁles por usuario,

datos indexados,

cuentas derivadas por seeds,

sin depender de una private key centralizada (foco de ataque).

Entonces Solana inventa un mecanismo:

El programa deriva cuentas previsibles, sin llaves privadas, y las maneja como si fuera su estado

interno.

![](data:image/png;base64...)

¿Cómo se genera una PDA?

Una PDA se deriva con:

PDA = hash(seeds..., program\_id")

Donde:

seeds: valores que deﬁnen la cuenta (pueden ser strings, pubkeys, u64…)

program\_id: asegura unicidad por programa

hash: debe generar una dirección off-curve

![](data:image/png;base64...)

¿Cómo se genera una PDA?

![](data:image/png;base64...)

¿Cómo se genera una PDA?

¿Qué signiﬁca “off-curve”?

Las direcciones de Solana (pubkeys) normalmente son puntos válidos en la curva Ed25519.

Pero las PDAs:

NO deben ser puntos válidos de la curva.

¿Por qué?

Porque si fueran válidos → podría existir una private key → alguien podría controlarlas → se rompe

la seguridad.

Al ser off-curve, la PDA NO tiene private key, solo existe como dirección válida.

![](data:image/png;base64...)

¿Cómo se genera una PDA?

¿Cómo ﬁrma una PDA si no tiene private key?

El runtime de Solana ﬁrma por la PDA cuando el programa presenta los seeds correctos.

El programa llama a:

invoke\_signed()

Y pasa:

&[&[seeds..., bump]]

El runtime:

Recalcula la PDA

Comprueba que coincide con la cuenta esperada

Autoriza la acción como si la PDA hubiera ﬁrmado

Esto evita sistemas custodiales y llaves privadas centralizadas.

![](data:image/png;base64...)

¿Cómo se genera una PDA?

¿Qué es el “bump”?

Es un número (u8) entre 0 y 255

Se usa para encontrar la primera dirección off-curve

Se agrega como seed extra

Debe guardarse siempre para derivar la misma PDA en el programa

Ejemplo:

let (pda, bump) =

Pubkey::ﬁnd\_program\_address(&[b"proﬁle", authority.key().as\_ref()], program\_id);

![](data:image/png;base64...)

Anchor

Anchor es un framework para escribir programas en Solana (en Rust) de forma segura, simple y con

menos código repetitivo.

Anchor se parece al equivalente de:

Truﬄe / Hardhat / Brownie en Ethereum

Anchor te da:

➢ Macros que genera mucho código repetitivo

➢ Validación automática de cuentas

➢ Soporte nativo para PDAs

➢ Cliente TypeScript autogenerado

➢ Errores personalizados

➢ Serialización automática (borsh)

Mecanismo de upgrade nativo

![](data:image/png;base64...)

Anchor

¿Qué problema resuelve Anchor?

En Solana “raw” (sin Anchor), escribir un programa implica:

➔ Validar manualmente cada cuenta

➔ Validar PDAs

➔ Validar owners

➔ Validar signers

➔ Veriﬁcar tamaños

➔ Serializar/deserializar bytes manualmente

➔ Manejar errores de forma artesanal

![](data:image/png;base64...)

Anchor

¿Cómo se estructura un programa Anchor?

El esquema básico es:

📁 programs/mi\_programa/src/lib.rs

![](data:image/png;base64...)

Anchor

El corazón de Anchor: Contexts

Cada instrucción tiene un Context, que deﬁne:

➔ Qué cuentas se reciben

➔ Qué permisos tiene cada cuenta

➔ Si son PDAs y bajo qué seeds

➔ Qué accounts son mutables

➔ Qué accounts son signers

![](data:image/png;base64...)

Anchor

Esto hace varias cosas automáticamente:

● Calcula la PDA

● Valida que es la PDA correcta

● Crea la cuenta con el tamaño exacto

● Calcula el rent (REMT) por vos

● Cobra los lamports necesarios

● Asegura que solo este programa pueda modiﬁcarla

● Valida signers

● Valida owners

● Valida permisos

![](data:image/png;base64...)

Anchor

Cómo se deﬁnen estructuras de cuentas

![](data:image/png;base64...)

Anchor

Cliente TypeScript automático

Anchor genera un cliente completo:

![](data:image/png;base64...)

Anchor

Errores custom y manejo seguro

![](data:image/png;base64...)

Anchor

Anchor Framework

anchor init nombre\_proyecto

anchor build

anchor test

anchor deploy

para ver la pubkey que va a realizar el deploy ejecutar el comando: solana address

la salida mostrara la pubkey para pedir fondos para poder desplegar el contrato en devnet

faucets para devnet:

https://faucet.solana.com/

https://www.devnetfaucet.org/

![](data:image/png;base64...)