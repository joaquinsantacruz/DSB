![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

![](data:image/png;base64...)

Conceptos

● Estándares más utilizados

● ERC-4337 (Account Abstraction / Smart Accounts)

● Patrones

● Oráculos y puentes

![](data:image/png;base64...)

Ethereum Request for Comment

Los estándares ERC (Ethereum Request for Comment) deﬁnen

reglas y convenciones que permiten la interoperabilidad entre

contratos y aplicaciones en la red Ethereum. Estos estándares

garantizan compatibilidad entre proyectos, evitan duplicación de

esfuerzos y aumentan la seguridad del ecosistema.

https://eips.ethereum.org/

![](data:image/png;base64...)

Ethereum Request for Comment

Cada número de estándar ERC, como ERC-20, ERC-721, etc.,

identiﬁca un estándar especíﬁco con reglas y características

particulares para un tipo de token o funcionalidad en Ethereum. Los

desarrolladores pueden seguir estos estándares para asegurarse de

que sus tokens y contratos inteligentes funcionan de manera

coherente con otros en la red, lo que facilita la integración y la

interacción entre diferentes aplicaciones y servicios basados en

Ethereum.

![](data:image/png;base64...)

Ethereum Request for Comment

Fungible- No fungible

El término "fungible" se reﬁere a la propiedad de un activo o un bien que es

intercambiable por otro de la misma clase o tipo de manera equivalente y

sin pérdida de valor. En otras palabras, si algo es fungible, signiﬁca que

una unidad de ese activo o bien es igual en valor y características a

cualquier otra unidad de la misma clase.

Por otro lado, los activos no fungibles (NFT) son aquellos que no son

intercambiables uno por uno de manera equivalente, ya que cada unidad

es única e indivisible.

![](data:image/png;base64...)

OpenZeppelin

es una de las principales bibliotecas de contratos inteligentes para

Ethereum y EVM. Proporciona implementaciones seguras y

auditadas de los estándares más utilizados (como ERC‑20, ERC‑721,

ERC‑1155) y patrones de seguridad, lo que permite a los

desarrolladores crear contratos conﬁables sin reinventar la rueda.

También ofrece herramientas para gestionar permisos,

actualizaciones y pruebas de seguridad

https://docs.openzeppelin.com/

https://docs.openzeppelin.com/contracts

![](data:image/png;base64...)

ERC20

Los tokens fungibles representan activos intercambiables (como monedas o puntos). En

Ethereum, el estándar ERC‑20 deﬁne la interfaz mínima para crear tokens fungibles.

La especiﬁcación original para ERC-20 se encuentra en el Ethereum Improvement

Proposal (EIP) número 20. Se puede consultar en el repositorio de GitHub de Ethereum o

en el sitio web oﬁcial de Ethereum EIP: https://eips.ethereum.org/EIPS/eip-20

documentación en openzeppelin: https://docs.openzeppelin.com/contracts/5.x/erc20

codigo del contrato:

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/

ERC20/ERC20.sol

![](data:image/png;base64...)

ERC20

ERC-20: La especiﬁcación original para ERC-20 se encuentra en el Ethereum

Improvement Proposal (EIP) número 20. Se puede consultar en el repositorio de

GitHub de Ethereum o en el sitio web oﬁcial de Ethereum EIP:

https://eips.ethereum.org/EIPS/eip-20

documentación en openzeppelin:

https://docs.openzeppelin.com/contracts/5.x/erc20

codigo del contrato:

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contract

s/token/ERC20/ERC20.sol

![](data:image/png;base64...)

ERC20

En un contrato ERC-20 (Ethereum Request for Comment 20), existen varios métodos/eventos estándar que

son considerados importantes y se utilizan comúnmente para interactuar con los tokens ERC-20.

balanceOf(address \_owner) returns (uint256): Este método permite consultar el saldo de tokens de una

dirección especíﬁca. Proporciona información sobre cuántos tokens ERC-20 posee una dirección determinada.

transfer(address \_to, uint256 \_value) returns (bool): Este método se utiliza para transferir tokens ERC-20 a

otra dirección. Es fundamental para realizar transacciones de tokens entre usuarios.

transferFrom(address \_from, address \_to, uint256 \_value) returns (bool): Este método se utiliza para permitir

que una dirección autorizada (generalmente a través del método approve) transﬁera tokens desde una

dirección a otra. Es esencial para implementar casos de uso como intercambios y contratos de tokens.

approve(address \_spender, uint256 \_value) returns (bool): Este método se utiliza para autorizar a una

dirección especíﬁca a gastar una cantidad especíﬁca de tokens en nombre del titular. Se utiliza en

combinación con transferFrom para permitir transacciones seguras y controladas.

allowance(address \_owner, address \_spender) returns (uint256): Este método permite consultar la cantidad

de tokens que una dirección autorizada (el "gastador") puede gastar en nombre del titular de los tokens.

![](data:image/png;base64...)

ERC20

Eventos:

Transfer(address indexed \_from, address indexed \_to, uint256 \_value): Este evento se emite cuando

se realiza una transferencia de tokens desde una dirección (\_from) a otra dirección (\_to). El índice

"indexed" se utiliza para facilitar la búsqueda de eventos especíﬁcos en registros de eventos.

Approval(address indexed \_owner, address indexed \_spender, uint256 \_value): Este evento se emite

cuando se aprueba a una dirección (\_spender) para gastar una cantidad especíﬁca de tokens en

nombre del titular (\_owner).

![](data:image/png;base64...)

ERC20: Extensiones modernas

ERC20Permit (EIP‑2612): ﬁrmas off‑chain para autorizar

transferencias sin enviar transacción (mejor UX/costos).

https://docs.openzeppelin.com/contracts/5.x/api/token/erc20#ERC

20Permit

ERC20Votes: agrega snapshots/ponderación para gobernanza.

https://docs.openzeppelin.com/contracts/5.x/api/token/erc20#ERC

20Votes

![](data:image/png;base64...)

ERC‑4626 — Tokenized Vaults

Bóvedas estandarizadas que tokenizan depósitos (DeFi).

https://eips.ethereum.org/EIPS/eip-4626

https://docs.openzeppelin.com/contracts/5.x/erc4626

![](data:image/png;base64...)

ERC721 (NFT)

ERC-721: La especiﬁcación original para ERC-721 se encuentra en el

Ethereum Improvement Proposal (EIP) número 721. Se puede consultar en

el repositorio de GitHub de Ethereum o en el sitio web oﬁcial de Ethereum

EIP: https://eips.ethereum.org/EIPS/eip-721

doc openzeppelin: https://docs.openzeppelin.com/contracts/5.x/erc721

implementación:

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/co

ntracts/token/ERC721/ERC721.sol

![](data:image/png;base64...)

ERC721

En un contrato ERC-721 (Ethereum Request for Comment 721), los métodos y eventos más importantes son aquellos que

permiten la creación y transferencia de tokens no fungibles (NFT), así como el seguimiento de estas acciones.

Métodos Principales:

balanceOf(address \_owner) returns (uint256): Permite consultar el saldo de tokens ERC-721 de una dirección especíﬁca.

Proporciona información sobre cuántos NFT posee una dirección determinada.

ownerOf(uint256 \_tokenId) returns (address): Este método permite determinar el propietario de un NFT especíﬁco

identiﬁcado por su ID de token (\_tokenId).

transferFrom(address \_from, address \_to, uint256 \_tokenId): Se utiliza para transferir la propiedad de un NFT de una

dirección (\_from) a otra dirección (\_to). Requiere que el remitente tenga permiso del propietario actual del NFT o que sea el

propietario actual.

approve(address \_approved, uint256 \_tokenId): Permite a un propietario de NFT otorgar permiso a otra dirección (\_approved)

para transferir un NFT especíﬁco (\_tokenId) en su nombre.

setApprovalForAll(address \_operator, bool \_approved): Este método permite a un propietario de NFT otorgar permiso a una

dirección (\_operator) para transferir todos sus NFT en su nombre (o revocar ese permiso).

![](data:image/png;base64...)

ERC721

Eventos Principales:

Transfer(address indexed \_from, address indexed \_to, uint256 indexed \_tokenId): Este evento se emite

cuando se realiza una transferencia exitosa de un NFT desde una dirección (\_from) a otra dirección (\_to).

Los índices "indexed" se utilizan para facilitar la búsqueda de eventos especíﬁcos.

Approval(address indexed \_owner, address indexed \_approved, uint256 indexed \_tokenId): Se emite

cuando un propietario de NFT otorga permiso a una dirección (\_approved) para transferir un NFT

especíﬁco (\_tokenId) en su nombre.

ApprovalForAll(address indexed \_owner, address indexed \_operator, bool \_approved): Se emite cuando

un propietario de NFT otorga o o revoca permiso a una dirección (\_operator) para transferir todos sus

NFT en su nombre.

![](data:image/png;base64...)

ERC‑1155

Múltiples tipos (fungibles y no fungibles) en un mismo contrato.

Optimiza gas y \*\*facilita operaciones masivas

(p. ej., mintear/enviar muchos IDs en una sola transacción).

https://docs.openzeppelin.com/contracts/5.x/erc1155

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

El estándar ERC‑4337 introduce Account Abstraction (AA):

cuentas de usuario que se comportan como contratos inteligentes

con lógica de validación propia (recuperación social, límites de gasto,

multiﬁrma, pagos de gas con tokens, etc.).

https://docs.openzeppelin.com/contracts/5.x/account-abstraction

Componentes clave:

EntryPoint (coordina operaciones), Bundlers (agregan UserOps),

Paymasters (pagan gas), Smart Account (reglas del usuario).

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

Flujo:

Usuario → Smart Account → Bundler → EntryPoint → Paymaster

(opcional) → Smart Account → Contrato destino

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

(1) El usuario prepara una UserOperation

En lugar de ﬁrmar una transacción, el usuario (o su app) crea una estructura

UserOperation:

Esta estructura se manda fuera de la blockchain a un Bundler (similar a un

“miner” de UserOps).

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

(2) El Bundler recoge varias UserOps

El Bundler junta muchas UserOperation y las mete en una sola

transacción que llama a:

EntryPoint.handleOps(userOps[], beneﬁciary);

Esa transacción sí se envía on-chain a través del EntryPoint (el

contrato central del sistema).

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

(3) El EntryPoint valida

El EntryPoint hace varias cosas importantes:

● Llama al método validateUserOp de cada Smart Account.

● veriﬁca la ﬁrma, el nonce, los límites, etc.

● Si hay un Paymaster, también llama a su validatePaymasterUserOp.

● ejecuta las operaciones (execute o call) del Smart Account.

Al ﬁnal, cobra las tasas de gas (al usuario o al Paymaster) y envía los fondos al

beneﬁciary (el Bundler).

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

4) La Smart Account ejecuta

En ese momento se realiza la acción real, igual que una transacción normal, pero

iniciada por lógica de contrato.

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

(5) El Paymaster (opcional) paga el gas

Si el usuario usa un Paymaster, éste valida que cubre los costos de gas.

Puede aplicar reglas: lista blanca, límites, staking, etc.

Luego, el EntryPoint le cobra el gas al Paymaster, no al usuario.

→ Esto permite “gasless transactions”.

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

![](data:image/png;base64...)

Account Abstraction y Smart Accounts

![](data:image/png;base64...)

Patrones de diseño

Los patrones de diseño de smart contracts son análogos a los

patrones de diseño de software en la programación tradicional, pero

están adaptados a las particularidades y desafíos de la blockchain.

Algunos de estos desafíos incluyen la inmutabilidad de los contratos,

las limitaciones en el uso de gas, la seguridad y la prevención de

ataques comunes como reentrancy attack.

![](data:image/png;base64...)

Patrones de diseño: check-Effects-Interactions

Este patrón previene ataques de reentrancia asegurando que todas

las interacciones externas se realicen después de actualizar el

estado del contrato. Más detalles y ejemplos en Solidity

Patterns(https://fravoll.github.io/solidity-patterns/checks\_effects\_interactions.html) y

una discusión general sobre su importancia en la seguridad de

Solidity en DEV

Community(https://dev.to/zaryab2000/the-signiﬁcance-of-check-effects-interaction-pattern-5hn6).

![](data:image/png;base64...)

Patrones de diseño: check-Effects-Interactions

![](data:image/png;base64...)

Patrones de diseño: check-Effects-Interactions

![](data:image/png;base64...)

Patrones de diseño

Circuit Breaker (Emergency Stop):este patrón generalmente implica

una funcionalidad que permite pausar o detener la interacción con el

contrato en situaciones de emergencia o anomalías.

![](data:image/png;base64...)

Patrones de diseño: Circuit Breaker (Emergency Stop)

![](data:image/png;base64...)

Patrones de diseño

Proxy or Upgrade Pattern: Permite actualizar contratos inteligentes

a pesar de su naturaleza inmutable.

![](data:image/png;base64...)

Patrones de diseño: Proxy or Upgrade

el ﬂujo general sería así:

a) Despliegue del Contrato de Implementación: Primero, se despliega el contrato Por ej SafeBank (o cualquier contrato que contenga tu lógica de

negocio) en la blockchain. Este contrato contiene las funciones/métodos que deseas que maneje la aplicación.

b) Despliegue del Contrato Proxy: Luego, se despliega el contrato Proxy, pasando la dirección del contrato SafeBank como parámetro al

constructor del Proxy. Esto establece el contrato de implementación inicial al que el Proxy delegará las llamadas.

c)Interacción a través del Proxy: Los usuarios interactúan con el contrato Proxy, no directamente con el SafeBank. Cuando un usuario llama a una

función en el Proxy, este contrato delega la llamada a SafeBank (o a la implementación actual).

d) Actualización: Si en el futuro se desea cambiar la lógica del contrato, se puede desplegar un nuevo contrato de implementación y luego llamar

a la función upgrade en el contrato Proxy para cambiar la dirección de la implementación al nuevo contrato. Esto permite actualizar la lógica del

contrato sin cambiar la dirección del contrato con el que los usuarios interactúan.

Es importante entender que el storage del estado de las estructuras queda en el contrato proxy y en caso de una actualización de la

implementación se deberá respetar las estructuras que fueron deﬁnidas sobre todo en el orden en que lo fueron para no romper accesos a la

memoria.

![](data:image/png;base64...)

Patrones de diseño: Proxy or Upgrade

![](data:image/png;base64...)

Patrones de diseño: Proxy or Upgrade

assembly { ... }: Indica el comienzo de un bloque de código de ensamblador en línea. Solidity permite el uso de ensamblador para operaciones de bajo nivel.

let ptr := mload(0x40): Esta línea asigna a ptr la dirección del espacio libre de memoria. mload(0x40) carga el contenido de la memoria en la dirección 0x40, que por

convención contiene el puntero al espacio libre de memoria.

calldatacopy(ptr, 0, calldatasize()): Copia los datos de la llamada entrante (calldata) al espacio de memoria libre. calldatacopy es una función de bajo nivel que copia los datos

de la llamada a una ubicación de memoria. ptr es el destino, 0 es el índice inicial de los datos de la llamada, y calldatasize() es el tamaño de los datos de la llamada.

let result := delegatecall(gas(), \_impl, ptr, calldatasize(), 0, 0): Realiza una llamada de delegación (delegatecall) al contrato en la dirección \_impl (el contrato de

implementación). Esta llamada utiliza todos los datos de gas disponibles, la dirección del contrato de implementación, y los datos de la llamada copiados en memoria.

delegatecall es similar a una llamada normal, pero mantiene el contexto del contrato que lo llama (en este caso, el contrato Proxy), incluyendo el almacenamiento y el

balance de ETH.

let size := returndatasize(): Después de que se ejecuta delegatecall, esta línea asigna a size el tamaño de los datos devueltos por la llamada.

returndatacopy(ptr, 0, size): Copia los datos devueltos por la llamada de delegación de vuelta a la memoria, empezando en la posición ptr.

switch result: Evalúa el resultado de la llamada de delegación.

case 0 { revert(ptr, size) }: Si result es 0, signiﬁca que la llamada de delegación falló. En este caso, se revierte toda la transacción y se devuelven los datos de error.

default { return(ptr, size) }: Si result no es 0, signiﬁca que la llamada fue exitosa. Los datos de retorno se envían de vuelta al llamador original.

![](data:image/png;base64...)

Patrones de diseño

Restricted Access: se reﬁere a restringir el acceso a ciertas

funciones del contrato solo a usuarios autorizados.

![](data:image/png;base64...)

Patrones de diseño

Pull Over Push for Payments:También conocido como "Secure

Withdrawal Pattern", este patrón sugiere que los contratos deben

permitir que los usuarios retiren fondos en lugar de enviarlos

directamente para mitigar riesgos.

![](data:image/png;base64...)

Patrones de diseño: Pull Over Push for Payments

![](data:image/png;base64...)

Patrones de diseño: Pull Over Push for Payments

![](data:image/png;base64...)

Patrones de diseño

Factory Contract Pattern: Involucra el uso de un contrato para crear

otros contratos.

![](data:image/png;base64...)

Patrones de diseño: Factory Contract

![](data:image/png;base64...)

Patrones de diseño:

Oracle Pattern: Los contratos inteligentes no pueden acceder

directamente a datos del mundo real. Los oráculos son servicios

externos que proveen estos datos. Este patrón gestiona cómo los

contratos interactúan con oráculos de manera segura y conﬁable.

![](data:image/png;base64...)

Patrones de diseño: Oracle

![](data:image/png;base64...)

Oráculos

Conceptos:

On-Chain: Hace referencia a todas las acciones, transacciones o datos que están

almacenados y veriﬁcados en la blockchain. Todo lo que es on-chain es inmutable y

transparente, formando parte del registro público de la blockchain. Las transacciones

on-chain requieren la veriﬁcación por parte de la red y consumen gas en Ethereum.

Off-Chain: Se reﬁere a las actividades o datos que no se registran en la blockchain. Estos

pueden incluir cálculos, procesamiento de datos o almacenamiento que se realiza fuera

de la cadena por razones de eﬁciencia, privacidad o costos. Las acciones off-chain

pueden ser más rápidas y menos costosas, pero no ofrecen la misma seguridad y

transparencia que las on-chain.

![](data:image/png;base64...)

Oráculos

Oráculo: es un sistema que proporciona datos del mundo real a la

cadena de bloques. Actúa como puente entre la blockchain (que es

un sistema cerrado y determinista) y fuentes de datos externas. Los

oráculos permiten a los contratos inteligentes reaccionar a eventos y

acceder a información fuera de la blockchain, que de otra manera

serían inaccesibles, como precios del mercado, resultados de

eventos, condiciones climáticas, etc. Son cruciales para muchas

aplicaciones descentralizadas que requieren datos externos para

operar eﬁcazmente.

![](data:image/png;base64...)

Oráculos

Algunas características:

Intermediarios de Datos: Facilitan la transferencia de datos del mundo real a la blockchain.

Fuente de Información Externa: Proveen información que no está inherentemente disponible en la blockchain, como precios

del mercado, resultados deportivos o datos climáticos.

Variedad de Fuentes: Pueden obtener datos de diversas fuentes, incluidas bases de datos, sitios web o dispositivos físicos

(IoT).

Conﬁanza y Seguridad: La conﬁabilidad de un oráculo es crítica, ya que los contratos inteligentes dependen de la exactitud de

los datos proporcionados.

Descentralización: Idealmente, los oráculos deben ser descentralizados para evitar puntos únicos de fallo y manipulación.

Integración con Contratos Inteligentes: Interactúan con contratos inteligentes para ejecutar acciones basadas en los datos

recibidos.

![](data:image/png;base64...)

Oráculos: chainlink

Chainlink es una red de oráculos descentralizada que permite que los contratos inteligentes en plataformas de

blockchain interactúen de manera segura con fuentes de datos externas, APIs y eventos del mundo real. Está compuesta

por una red de nodos llamados "nodos Chainlink" que recuperan y veriﬁcan datos fuera de la cadena y luego los entregan

a los contratos inteligentes. La naturaleza descentralizada y resistente a la manipulación de Chainlink garantiza la

conﬁabilidad y precisión de los datos, lo que lo convierte en un componente crítico para habilitar aplicaciones de

contratos inteligentes sin necesidad de conﬁanza y ricas en datos en diversas industrias, incluyendo DeFi, seguros,

cadena de suministro y más. Utiliza su criptomoneda nativa, LINK, para varias funciones dentro de la red, incluyendo

incentivos para nodos y pagos por solicitudes de datos.

mas info: https://research.chain.link/whitepaper-v2.pdf

![](data:image/png;base64...)

Chainlink

![](data:image/png;base64...)

Chainlink

![](data:image/png;base64...)

Chainlink: cu

https://docs.chain.link/ccip/tutorials/cross-chain-tokens

https://docs.chain.link/ccip/tutorials/programmable-token-transfers

https://docs.chain.link/ccip/tutorials/send-arbitrary-data

https://docs.chain.link/chainlink-automation/guides/compatible-contracts

https://dev.chain.link/products/data

![](data:image/png;base64...)

Puentes e Interoperabilidad Cross‑Chain

Las blockchains son como islas: necesitamos puentes para mover activos y

mensajes entre cadenas. Riesgos históricos: veriﬁcación defectuosa, validadores

comprometidos, wrapping con bugs.

![](data:image/png;base64...)

Puentes e Interoperabilidad Cross‑Chain

Chainlink CCIP

Protocolo moderno para mensajería + tokens entre redes con seguridad multicapa.

https://docs.chain.link/ccip/tutorials/cross-chain-tokens

Usuario

↓

CrossChainSender (en red origen)

↓ → crea mensaje (receiver, data)

↓ → llama a ccipSend()

↓

Chainlink Router (on-chain)

↓ → red de nodos Chainlink

↓

Chainlink Router (en red destino)

↓

CrossChainReceiver (en red destino)

↓

Ejecución del mensaje o acción ﬁnal

![](data:image/png;base64...)

Puentes e Interoperabilidad Cross‑Chain

![](data:image/png;base64...)

Puentes e Interoperabilidad Cross‑Chain

![](data:image/png;base64...)

Seguridad y Auditoría

La seguridad es esencial por la inmutabilidad. A continuación, más vulnerabilidades clave con ejemplos y mitigaciones.

Front‑running (Sandwich Attacks)

Riesgo por MEV/mempool. Mitigar con commit‑reveal, precios ﬁjos por bloque o canales privados.

MEV: https://ethereum.org/en/developers/docs/mev/

Integer overﬂow/underﬂow:

Usar Solidity 0.8+ (revierten por defecto) o `SafeMath` en versiones antiguas.

Notas 0.8.0: https://docs.soliditylang.org/en/v0.8.0/080-breaking-changes.html

Uso incorrecto de delegatecall

Usar proxies auditados (Transparent/UUPS), onlyAdmin y validar implementaciones.

EIP‑1967: https://eips.ethereum.org/EIPS/eip-1967

![](data:image/png;base64...)

OWASP Smart Contract Top 10

es un documento de concientización estándar que tiene como objetivo brindar

a los desarrolladores y equipos de seguridad de Web3 información sobre las 10

principales vulnerabilidades encontradas en los contratos inteligentes.

https://owasp.org/www-project-smart-contract-top-10/

![](data:image/png;base64...)