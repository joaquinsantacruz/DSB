![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

Clase

![](data:image/png;base64...)

Conceptos

● Web3: la capa de propiedad del Internet

● Trilema blockchain y modularidad

● Layer 2 y Layer 3

● Bridges y mensajería cross-chain

● Ecosistema Omnichain

● AI + Web3 (agentes inteligentes)

● Account Abstraction (smart wallets)

● web3.py (interacción con blockchain)

![](data:image/png;base64...)

Web3: la capa de propiedad y coordinación del Internet

representa la evolución de Internet hacia un modelo en el que los usuarios poseen y controlan su identidad,

sus datos y sus activos digitales.

Es la capa de propiedad, conﬁanza y coordinación del nuevo Internet, construida sobre blockchains públicas,

protocolos abiertos y contratos inteligentes.

A diferencia de la Web2 —controlada por plataformas centralizadas— la Web3 devuelve al usuario el control

mediante wallets, que actúan como su identidad digital universal.

Hoy Web3 integra blockchain, identidad descentralizada (DID), IA, infraestructura física descentralizada

(DePIN) y activos del mundo real (RWA), formando el Internet de la Propiedad.

Ya no hablamos de una web paralela o futurista. Web3 es la capa de propiedad del Internet actual. Es donde

los usuarios, y también las máquinas, pueden tener activos y operar de forma autónoma

![](data:image/png;base64...)

Web3: principios fundamentales

1. Propiedad y control personal: identidad y activos gestionados mediante smart wallets y account abstraction

(sin depender de claves privadas).

2. Descentralización efectiva: no solo en infraestructura, sino también en gobernanza (DAO, restaking,

validadores distribuidos).

3. Interoperabilidad y modularidad: comunicación entre cadenas mediante bridges, rollups y cross-chain

messaging (LayerZero, Wormhole, Axelar).

4. Modelos económicos participativos: los usuarios comparten valor (staking, yield, gobernanza).

5. Transparencia veriﬁcable: la conﬁanza proviene del código abierto y la criptografía.

6. Integración con IA y DePIN: agentes inteligentes y hardware comunitario participando en la red.

7. RWA y economía global tokenizada: representación digital de activos físicos y ﬁnancieros.

![](data:image/png;base64...)

Trilema blockchain

término popularizado por Vitalik Buterin, cofundador de Ethereum, describe el dilema enfrentado

por las blockchains en términos de navegación entre tres propiedades principales: seguridad,

escalabilidad y descentralización. Según el trilema, una blockchain no puede maximizar

simultáneamente estas tres propiedades; siempre debe comprometer al menos una de ellas

para fortalecer las otras dos.

![](data:image/png;base64...)

El Trilema Blockchain y su evolución modular

El trilema sigue siendo una referencia, pero las blockchains actuales buscan resolverlo mediante

la modularidad.

🔹 Seguridad compartida: mecanismos de restaking (EigenLayer, Babylon) permiten reutilizar el

stake de Ethereum para proteger otras cadenas.

🔹 Escalabilidad modular: capas separadas para consenso, ejecución y disponibilidad de datos

(Celestia, Avail, Solana Firedancer).

🔹 Descentralización adaptable: nuevas formas de gobernanza y validación, como DAOs o

rollups soberanos.

💡 La nueva generación de blockchains ya no elige entre las tres propiedades: las combina en un

sistema modular cooperativo

![](data:image/png;base64...)

Layer 2, Layer 3 y la era de la modularidad

Las Layer 2 (L2) procesan transacciones fuera de la cadena principal (L1), aumentando velocidad y reduciendo costos.

Aparecen también las Layer 3 (L3) y las Data Availability Layers (DA), extendiendo el modelo modular.

● Ejemplos de L2:

○ Optimistic Rollups: Base, Arbitrum, Optimism.

○ zk-Rollups: zkSync, Scroll, Polygon zkEVM.

● Ejemplos de L3 y DA Layers:

○ Xai Network (gaming chain sobre Arbitrum).

○ Celestia, Avail (almacenamiento de datos veriﬁcados).

➢ Ethereum evoluciona hacia una red de redes.

Cada capa cumple un rol especíﬁco dentro del ecosistema global.

![](data:image/png;base64...)

L2: Categorías

1. Canales de Estado: Lightning Network en Bitcoin.

Los canales de estado permiten a los usuarios realizar transacciones entre ellos fuera de la cadena

principal (off-chain) y luego ﬁnalmente asentar el estado ﬁnal de todas las transacciones en la cadena

principal.

2. Rollups: Optimistic Rollups, zk-Rollups.

Los rollups ejecutan transacciones fuera de la cadena y suben a la blockchain principal un resumen

criptográﬁco de esas transacciones, junto con una prueba que puede ser veriﬁcada por otros

participantes en la red.

Optimistic Rollups: Las transacciones se ejecutan primero en L2 y las disputas sobre la validez de las

transacciones se resuelven en L1.

zk-Rollups: Todas las transacciones son válidas por defecto en L2 gracias al uso de pruebas de conocimiento cero

(zk-SNARKs) que se veriﬁcan en L1.

![](data:image/png;base64...)

L2: Categorías

3. Sidechains: xDai, Polygon (antes Matic).

Las sidechains son blockchains separadas que están pegadas a la blockchain principal. Los tokens y

otros activos pueden ser movidos entre la cadena principal y la sidechain, pero la sidechain opera con

un consenso independiente y, a menudo, con reglas y capacidades diferentes.

4. Plasma:

Plasma implica la creación de blockchains hijos que se derivan de la cadena principal. Los blockchains

hijos (Plasma Chains) pueden procesar transacciones y contratos inteligentes en su propia red y luego

publican el estado de esas transacciones en la cadena principal.

![](data:image/png;base64...)

Bridge

Un bridge (puente) en el contexto de la tecnología blockchain se reﬁere a un

protocolo que permite la transferencia de tokens y/o datos entre dos

blockchains independientes. Los puentes buscan mejorar la

interoperabilidad entre diferentes redes blockchain, permitiendo que los

activos y la información se muevan de manera ﬂuida entre diferentes

plataformas.

![](data:image/png;base64...)

Tipos de bridges

1- Token Bridges: Permiten la transferencia de tokens entre dos blockchains.

Los tokens pueden ser representaciones de activos existentes (por ejemplo, tokens estables, tokens de

criptomonedas, tokens de activos reales) y se bloquean en una cadena mientras están activos en la

otra.

2- Data Bridges: Facilitan la transferencia de datos e información entre blockchains.

Esto es crucial para la operación de oráculos descentralizados y para que los smart contracts en

diferentes cadenas interactúen entre sí.

3- NFT Bridges: Permiten la transferencia de tokens no fungibles (NFTs) entre diferentes blockchains.

Los NFTs se bloquean en una cadena y se representan en otra para preservar la unicidad y la propiedad

del activo.

![](data:image/png;base64...)

Bridges: Mecanismos Comunes de Funcionamiento

●  Locking and Minting: Un activo se bloquea en una blockchain y se crea (mintea) una

representación de ese activo en la cadena de destino.

●  Multi-Signature Wallets: Las transacciones a menudo requieren ﬁrmas de múltiples partes para

validar la transferencia de fondos entre cadenas.

● Relayers: Los relayers son nodos que facilitan la comunicación entre las blockchains involucradas

en el puente, a menudo retransmitiendo pruebas o eventos de una cadena a otra.

● Smart Contracts: Los puentes utilizan contratos inteligentes para administrar el bloqueo, minteo y

la quema de tokens, y para validar las pruebas y datos de la cadena opuesta.

![](data:image/png;base64...)

Bridges y mensajería cross-chain

Los puentes tradicionales fueron esenciales para la interoperabilidad, pero también los más vulnerables.

En su lugar surgen los protocolos de mensajería cross-chain, que no mueven tokens, sino mensajes

veriﬁcados criptográﬁcamente.

🔹 Ejemplos modernos:

LayerZero: mensajería omnichain sin “lock & mint”.

Axelar, Wormhole: veriﬁcación criptográﬁca entre cadenas.

Circle CCTP: permite mover USDC nativo sin “wrapped tokens”.

🔒 Enfoque actual: seguridad mediante zk proofs, light clients y validadores compartidos.

![](data:image/png;base64...)

Concepto de Multichain

se reﬁere a la interoperabilidad y la interacción entre múltiples blockchains.

● Interoperabilidad: La capacidad de interactuar e intercambiar datos y valor entre diferentes

blockchains.

● Escalabilidad: Utiliza múltiples cadenas de bloques para distribuir la carga y mejorar la

escalabilidad del sistema.

● Optimización: Permite la utilización de diferentes blockchains para diferentes usos, cada

una optimizada para un caso de uso particular. Gaming, DeFi, etc

![](data:image/png;base64...)

De Multichain a Omnichain

La Web3 actual evoluciona hacia un modelo omnichain, donde las aplicaciones y los activos funcionan

en múltiples blockchains simultáneamente.

🔹 Ejemplos:

UniswapX: permite swaps entre cadenas con un solo clic.

Jupiter (Solana): enruta liquidez cross-chain automáticamente.

Wormhole, LayerZero, Axelar: capas de interoperabilidad entre ecosistemas.

El usuario ya no necesita saber en qué red está.

La interoperabilidad se convierte en una experiencia invisible e integrada.

![](data:image/png;base64...)

DePIN: infraestructura física descentralizada

DePIN integra hardware y blockchain para crear redes físicas colaborativas.

Personas o empresas aportan recursos físicos (computación, conectividad, almacenamiento, energía) y

reciben tokens por su participación.

🔹 Ejemplos destacados:

○ Helium: red 5G e IoT descentralizada.

○ Render Network: renderizado 3D distribuido.

○ io.net: computación descentralizada para IA.

○ Filecoin, Arweave: almacenamiento descentralizado.

DePIN representa la tokenización de la infraestructura global.

![](data:image/png;base64...)

RWA: tokenización de activos del mundo real

Los RWA conectan la economía tradicional con la blockchain, permitiendo representar activos del

mundo real en forma de tokens.

🔹 Tipos de RWA:

● Financieros: bonos del Tesoro, créditos tokenizados.

● Inmobiliarios: propiedades fraccionadas en tokens.

● Commodities: oro, energía, materias primas.

● Productivos: facturas, préstamos, producción agrícola.

🔹 Ejemplos reales:

● BlackRock y Franklin Templeton usando Ethereum para bonos.

● MakerDAO integrando RWA para colateral estable.

Los RWA son el puente entre la economía real y el mundo blockchain.

![](data:image/png;base64...)

AI + Web3: agentes inteligentes con wallets

La combinación de inteligencia artiﬁcial y blockchain da origen a los AI Agents, entidades digitales

capaces de poseer activos y ejecutar acciones autónomas on-chain.

🔹 Capacidades:

● Administrar fondos y ﬁrmar transacciones.

● Interactuar con contratos inteligentes.

● Analizar datos y ejecutar estrategias.

🔹 Ejemplos:

● Fetch.ai / Autonolas: agentes autónomos descentralizados.

● Alethea AI: avatares digitales inteligentes con identidad blockchain.

● Solana AI Agents: agentes integrados en wallets.

La IA se convierte en un actor económico dentro del ecosistema Web3.

![](data:image/png;base64...)

Account Abstraction: el nuevo estándar de interacción

(AA) introduce cuentas programables que reemplazan el modelo tradicional de wallets controladas por

claves privadas.

🔹 Ventajas clave:

● Recuperación social (sin pérdida de acceso).

● Transacciones “gasless” patrocinadas por la dApp.

● Pagos de gas con stablecoins.

● Lógica personalizada: límites, multisig, automatización.

🔹 Implementaciones:

● ERC-4337 en Ethereum.

● Safe (ex Gnosis Safe) y Biconomy Smart Accounts.

● Backpack (Solana) con wallets programables.

Las wallets se vuelven inteligentes, conﬁgurables y seguras.

![](data:image/png;base64...)

Web3 hoy: la capa de propiedad del Internet

La Web3 moderna integra todos estos conceptos en un ecosistema interconectado:

● Identidad soberana (DID, ENS, Solana Names)

● Account Abstraction y Smart Wallets

● Agentes de IA con propiedad digital

● DePIN: infraestructura física descentralizada

● RWA: tokenización de activos del mundo real

● Cadenas modulares, interoperables y omnichain

La Web3 ya no es una promesa: es la infraestructura económica global de Internet descentralizada.

En en 2017 se hablaba de ICOs y en 2020 de DeFi, en 2025 hablamos de identidad, activos reales,

infraestructura física y agentes inteligentes. La Web3 se convirtió en el sistema operativo económico de

Internet

![](data:image/png;base64...)

Web3: clientes

![](data:image/png;base64...)

Web3: clientes

un cliente web3 es una colección de bibliotecas que permiten interactuar con un nodo local o remoto de

alguna blockchain, utilizando una conexión HTTP, RPC o WebSocket. Es esencialmente la "puerta de

entrada" que permite a las aplicaciones en la web interactuar con la blockchain. Ls versiones más

conocidas de estas bibliotecas son web3.js y web3.py, aunque hay implementaciones en otros

lenguajes.

![](data:image/png;base64...)

Web3: clientes - características

1. Conexión con la Blockchain: Permite conectarse a la red a través de un proveedor (por ejemplo, un nodo

local como Geth o servicios como Infura).

2. Interacción con Contratos Inteligentes: Una vez obtenido el ABI (Application Binary Interface) de un

contrato, se puede usar `web3` para interactuar con ese contrato: leer datos, enviar transacciones, etc.

3. Construcción y Envío de Transacciones: Se puede construir transacciones, ﬁrmarlas y luego enviarlas a la

red.

4. Consulta de Datos: Se puede consultar datos de la blockchain, como el balance de una dirección, el estado

de una transacción, o la información de un bloque.

5. Utils: también viene con una serie de utils para realizar tareas como convertir valores entre Ether y Wei, o

calcular el hash de una serie de datos.

es esencial para cualquier dapp (aplicación descentralizada), ya que facilita la interacción entre la parte frontal (frontend) de la aplicación y la

blockchain.

![](data:image/png;base64...)

Web3py

necesitaremos:

1- Url de nodo para conectarnos para leer información o enviar una

transacción, aquí podremos utilizar algún servicio, buscar algún nodo

público o levantar un nodo propio.

2- una privada donde su pública tenga fondos para realizar transacciones.

![](data:image/png;base64...)

Web3py

1- para simpliﬁcar podemos utilizar como proveedor: infura o alchemy

2- usaremos alguna pk de una billetera cargada previamente con fondos.

3- la doc oﬁcial está en: https://web3py.readthedocs.io/en/stable/

![](data:image/png;base64...)

Web3py: conectando a un nodo

#pip install web3

from web3 import Web3

import os

NODE = os.environ.get("NODE")

w3 = Web3(Web3.HTTPProvider(NODE))

w3.isConnected()

![](data:image/png;base64...)

Web3py: obteniendo info del último bloque y la pública de una pk

print(w3.eth.get\_block('latest'))

account = w3.eth.account.from\_key(os.environ.get("pk"))

print(account.address)

![](data:image/png;base64...)

Web3py: enviando fondos

signed\_txn = w3.eth.account.sign\_transaction({

"nonce":w3.eth.get\_transaction\_count(account.address),

"gas":21000,

"gasPrice":w3.eth.gasPrice,

"to":"0x27227775d3dd9a6b5A9F1DD02761470E7D7EA466",

"value":1\*10\*\*17 ,#en wei esto seria 0.1 ETH

"chainId":5,

},

os.environ.get("pk")

)

tx\_hash = w3.eth.send\_raw\_transaction(signed\_txn.rawTransaction)

![](data:image/png;base64...)

Web3py: obteniendo data de una tx

txn\_hash = "0x6aa5347995e7f468153f099d5a962e556203a000d643848b60f9bdd522e0910e"

data = w3.eth.get\_transaction (txn\_hash)

![](data:image/png;base64...)

Para leer data de un contrato, aparte de la address del mismo necesitamos el ABI.

abi = """[{

"inputs": [],

"stateMutability": "nonpayable",

"type": "constructor"

},

{

"inputs": [],

"name": "increment",

"outputs": [],

"stateMutability": "nonpayable",

"type": "function"

},

{

"inputs": [],

"name": "retrieve",

"outputs": [

{

"internalType": "uint256",

"name": "",

"type": "uint256"

}

],

"stateMutability": "view",

"type": "function"

}

]"""

contract\_address = w3.toChecksumAddress("0x2b5aadd271f1f1a1e7468d0e9abb5907ae6a4af2")

Web3py: leyendo data de un contrato

![](data:image/png;base64...)

mi\_contrato = w3.eth.contract(

address=contract\_address,

abi=abi

)

mi\_contrato.functions.retrieve().call()

Web3py: leyendo data de un contrato

![](data:image/png;base64...)

Web3py: escribiendo en un contrato

tx = {

"nonce" :w3.eth.get\_transaction\_count (account .address),

"gas":200000 ,

"gasPrice" :w3.eth.gasPrice,

"value" :0 ,

"chainId" :5,

}

contract\_data  = mi\_contrato .functions.increment().buildTransaction( tx)

signed\_txn  = w3.eth.account .signTransaction( contract\_data , os.environ .get("pk"))

txn\_hash = w3.eth.sendRawTransaction(signed\_txn.rawTransaction)

![](data:image/png;base64...)

Web3py: escribiendo en un contrato, calculando el gas

#estimando el gas

tx = {

"nonce":w3.eth.get\_transaction\_count (account.address),

"gasPrice" :w3.eth.gasPrice,

"value":0 ,

"chainId" :5,

}

contract\_data  = mi\_contrato .functions.increment().buildTransaction( tx)

estimated\_gas  = w3.eth.estimateGas( contract\_data )

tx['gas'] = estimated\_gas

contract\_data  = mi\_contrato .functions.increment().buildTransaction( tx)

signed\_txn  = w3.eth.account.signTransaction( contract\_data , os.environ.get("pk"))

txn\_hash = w3.eth.sendRawTransaction( signed\_txn .rawTransaction)

![](data:image/png;base64...)

Web3py: obteniendo las txs de la mempool

# Obtener el bloque "pending", que representa el conjunto actual de transacciones

pendientes

pending\_block = w3.eth.getBlock('pending')

# Extraer las transacciones del bloque pendiente

pending\_transactions = pending\_block['transactions']

# Imprimir las transacciones pendientes

for tx in pending\_transactions:

print(tx)

# Si deseas obtener los detalles completos de cada transacción, puedes hacerlo con:

for tx\_hash in pending\_transactions:

tx = w3.eth.getTransaction(tx\_hash)

print(tx)

![](data:image/png;base64...)

Web3py: api leer data

![](data:image/png;base64...)

Web3py: api escribir data

![](data:image/png;base64...)

Web3py: api contrato

![](data:image/png;base64...)

Web3py: api eventos

![](data:image/png;base64...)