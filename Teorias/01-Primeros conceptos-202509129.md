![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

Bienvenid@s!

![](data:image/png;base64...)

Metodología

● Clases virtuales teórico-prácticas que luego se suben a youtube

● Comunicación y consultas por discord

![](data:image/png;base64...)

● Para obtener la cursada:

○ Resolución de todos los cuestionarios semanales online.

○ Aprobación de la mitad de los cuestionarios.

○ Entregas individuales parciales de ejercicios de las prácticas.

● Para aprobar la materia:

○ Desarrollo de un tp ﬁnal integrador

Como se aprueba la materia

![](data:image/png;base64...)

Primeros conceptos

● Criptografía

● Blockchain

● Transacción

● Bitcoin

● Algoritmo ECDSA

● Algoritmo SHA-256

● Algoritmo de consenso: PoW

● Frase semilla

● UTXO

![](data:image/png;base64...)

Criptografía

![](data:image/png;base64...)

Criptografía

La criptografía es un campo de estudio que se ocupa de asegurar la comunicación y

el almacenamiento de información mediante técnicas de codiﬁcación y

descodiﬁcación.

Técnicamente, la criptografía se basa en algoritmos matemáticos que transforman la

información original (texto plano o datos sin cifrar) en una forma ilegible llamada

texto cifrado o criptograma.

![](data:image/png;base64...)

Criptografía

Existen dos categorías principales de criptografía:

Criptografía simétrica: Utiliza la misma clave tanto para cifrar como para descifrar la

información. Ambas partes (emisor y receptor) deben compartir y mantener en secreto

esta clave. Ejemplos de algoritmos simétricos incluyen DES, AES y RC4.

Criptografía asimétrica (o de clave pública): Utiliza un par de claves(una pública y una

privada). Lo que se cifra con una clave solo puede ser descifrado con la otra y viceversa.

La clave pública puede ser compartida libremente, mientras que la clave privada se

mantiene en secreto. Los sistemas de clave pública son esenciales para muchas

aplicaciones en línea, incluidas las ﬁrmas digitales y el cifrado de correo electrónico.

Ejemplos de criptografía asimétrica incluyen RSA, DSA y ECDSA.

![](data:image/png;base64...)

Criptografía

Además de cifrar y descifrar información, la criptografía también se utiliza para:

Firmas digitales: Proporcionan una forma de veriﬁcar la autenticidad y la

integridad de los datos. Una ﬁrma digital es un dato que se genera a partir de un

mensaje y una clave privada, y puede ser veriﬁcado por cualquier persona que

tenga la clave pública correspondiente y el mensaje original.

Funciones hash criptográﬁcas: Estas funciones toman una entrada (o "mensaje")

y devuelven una cadena ﬁja de bytes. La salida, típicamente un valor de hash,

debería ser única (o muy difícil de repetir) para cada entrada única. Es

computacionalmente difícil generar la misma salida hash a partir de dos

entradas diferentes. Ejemplos incluyen SHA-256 y RIPEMD-160.

![](data:image/png;base64...)

Blockchain

![](data:image/png;base64...)

Blockchain

Es una estructura de datos en la que los bloques se enlazan secuencialmente. Cada

bloque tiene una referencia al bloque anterior mediante un hash criptográﬁco. Esto

crea una cadena de bloques que proporciona integridad y seguridad a los datos

almacenados, ya que cualquier modiﬁcación en un bloque afectaría a todos los

bloques siguientes.

![](data:image/png;base64...)

Blockchain: Bloque

Un bloque contiene la siguiente información:

❖ Un hash que lo identiﬁca.

❖ Una marca de tiempo.

❖ Referencia del bloque anterior.

❖ Transacciones del bloque.

![](data:image/png;base64...)

Blockchain: Transacción

Una transacción contiene la siguiente información:

❖ Un hash que la identiﬁca.

❖ El bloque al que pertenece.

❖ Un remitente.

❖ Un receptor.

❖ Valor enviado.

❖ Una marca de tiempo.

❖ Está ﬁrmada criptográﬁcamente.

![](data:image/png;base64...)

Blockchain: Transacción

![](data:image/png;base64...)

Blockchain: Nodo

Un nodo se reﬁere a un dispositivo o computadora que participa en la red de

blockchain. Cada nodo tiene una copia de la cadena de bloques completa o una parte

de ella, dependiendo de la arquitectura de la red. Los nodos son responsables de

mantener la integridad de la red y de validar las transacciones y los bloques.

Los nodos se comunican entre sí para compartir información y mantener la

consistencia de la red. Su participación en la red permite la descentralización y la

conﬁanza en la seguridad y la validez de las transacciones en blockchain.

![](data:image/png;base64...)

Blockchain: Nodo

![](data:image/png;base64...)

Blockchain: Ciclo de vida de una txn

1. Creación y ﬁrma

2. Propagación a la red

3. Espera en el mempool

4. Un validador o minero la selecciona

5. Se agrega a un bloque y es validado.

6. Conﬁrmación de la transacción

![](data:image/png;base64...)

Blockchain: Validación de una txn

La validación de una transacción en blockchain es el proceso mediante el cual se

veriﬁca y conﬁrma la autenticidad y la integridad de la transacción antes de ser

registrada en la cadena de bloques. Los nodos de la red de blockchain, utilizando

reglas y protocolos predeﬁnidos, revisan la validez de la transacción, asegurándose

de que cumpla con los requisitos y las reglas establecidas. Esto puede implicar

veriﬁcar la ﬁrma digital, comprobar el saldo suﬁciente del remitente y aplicar las

reglas de consenso para evitar transacciones fraudulentas o inválidas. Una vez

validada, la transacción se agrega a un bloque y se propaga a través de la red para su

posterior conﬁrmación y consenso por parte de los nodos.

![](data:image/png;base64...)

Bitcoin

![](data:image/png;base64...)

Bitcoin(2009)

Blockchain inicialmente propuesta en el 2009: https://bitcoin.org/bitcoin.pdf

Características técnicas en su implementación:

❏ Hashing SHA-256: El algoritmo Secure Hash Algorithm 256-bit (SHA-256) es la

función de hash principal utilizada en Bitcoin. Esta función toma datos de

entrada y devuelve una cadena de 256 bits que parece aleatoria.

❏ Criptografía de clave pública(asimétrica): Cada usuario tiene un par de

claves(una clave pública y una clave privada). Utiliza el algoritmo de ﬁrma digital

Elliptic Curve Digital Signature Algorithm (ECDSA) para este propósito.

![](data:image/png;base64...)

Pero, qué es una curva elíptica?

Una curva elíptica, en términos matemáticos, es el conjunto de puntos que

satisfacen una ecuación especíﬁca de la forma:

y

2

= x

3

+ax+b

donde a y b son constantes y la curva está deﬁnida sobre un campo (como los

números reales, números complejos o un campo ﬁnito).

![](data:image/png;base64...)

Curva elíptica

La elección de una curva elíptica para uso criptográﬁco es esencial y no es trivial. Elegir una curva

adecuada puede ser la diferencia entre un sistema seguro y un sistema vulnerable. La elección de la

curva implica tanto criterios matemáticos como consideraciones prácticas.

Puntos importantes:

➢ Número de puntos: a mayor número de puntos mayor seguridad en la criptografía.

➢ Propiedades matemáticas: fundamental que no tenga propiedades matemáticas que la hagan

vulnerable a ataques. Por ejemplo, algunas curvas tienen un número pequeño de puntos, lo

que las hace inseguras. Otras pueden tener estructuras algebraicas que las hagan

susceptibles a ciertos ataques.

![](data:image/png;base64...)

Bitcoin: curva elíptica -> secp256k1

La ecuación de la curva secp256k1 en su forma canónica es:

y

2

= x

3

+7

Esta ecuación está deﬁnida sobre un campo primo de tamaño

2

256

−2

32

−977

Dentro del contexto de Bitcoin y la criptografía de curvas elípticas, esta curva se

utiliza para el algoritmo de ﬁrma digital ECDSA (Elliptic Curve Digital Signature

Algorithm). Las propiedades de la curva y el gran tamaño del campo subyacente

contribuyen a la seguridad de las ﬁrmas y claves en el sistema de Bitcoin.

![](data:image/png;base64...)

Bitcoin: curva elíptica -> secp256k1

La cantidad exacta de puntos N (orden de la curva) es un número primo muy grande que se utiliza

en la criptografía de curvas elípticas para deﬁnir el grupo ﬁnito de puntos sobre el cual se realizan las

operaciones.

El orden N de la curva secp256k1 es:

N

=115792089237316195423570985008687907852837564279074904382605163141518161494337

Esto signiﬁca que hay exactamente N puntos en el grupo generado por el punto base de la curva.

Este orden es fundamental para la seguridad del ECDSA y otros protocolos de criptografía basados

en curvas elípticas, ya que garantiza que las operaciones se realicen en un grupo de tamaño

conocido y suﬁcientemente grande. Las operaciones matemáticas (como la suma y la

multiplicación de puntos) dentro del contexto criptográﬁco se realizan módulo N.

![](data:image/png;base64...)

Bitcoin: curva elíptica -> secp256k1

# ejemplo1.py

# pip install numpy

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)

y = np.sqrt(x\*\*3 + 7)

plt.plot(x, y, label="y^2 = x^3 + 7", color='blue')

plt.plot(x, -y, color='blue')

plt.legend()

plt.title("Visualización de secp256k1 en el espacio real")

plt.xlabel("x")

plt.ylabel("y")

plt.grid(True)

plt.show()

![](data:image/png;base64...)

Bitcoin: Generación de claves

❖ Se elige un punto base de la curva (G), que es ﬁjo y conocido públicamente.

❖ Se selecciona un número aleatorio como clave privada en el rango [1,N-1] con

gran entropía.

❖ Se multiplica este número (la clave privada) por el punto base de la curva elíptica

para obtener un nuevo punto: ese punto es la clave pública.

![](data:image/png;base64...)

Bitcoin: Generación de claves

# ejemplo2.py

# pip install ecsda

from ecdsa import SigningKey , SECP256k1, VerifyingKey

# Generando una clave privada para la curva secp256k1

sk = SigningKey .generate(curve=SECP256k1 )

# Obteniendo la clave pública a partir de la clave privada

vk = sk.get\_verifying\_key ()

# Imprimiendo la clave privada y pública

print("Private Key:" , sk.to\_string().hex())

print("Public Key:" , vk.to\_string().hex())

![](data:image/png;base64...)

Bitcoin: SHA-256

Hashing SHA-256: El algoritmo Secure Hash Algorithm 256-bit (SHA-256) es la

función de hash principal utilizada en Bitcoin. Esta función toma datos de

entrada y devuelve una cadena de 256 bits que parece aleatoria. Cualquier

cambio, por pequeño que sea, en los datos de entrada produce un hash

completamente diferente. Las transacciones y bloques en la cadena de bloques

de Bitcoin se identiﬁcan y veriﬁcan mediante este algoritmo de hash.

![](data:image/png;base64...)

Bitcoin: SHA-256

import  hashlib

#ejemplo3.py

def double\_sha256 (data):

"""Aplica SHA-256 dos veces."""

return  hashlib .sha256 (hashlib .sha256 (data).digest()).digest ()

# Entrada ficticia: hash de transacción anterior y el índice de la salida

input\_txid  = "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"

input\_vout  = "00000000"

# Salida ficticia: cantidad en satoshis (0.1 BTC) y un scriptPubKey ficticio

output\_value  = "00ca9a3b00000000"

# Juntar todos los componentes para formar la estructura de la transacción serializada

raw\_transaction  = input\_txid  + input\_vout  + output\_value

# Convertir la transacción en bytes

transaction\_bytes  = bytes.fromhex (raw\_transaction )

# Generar el hash de la transacción

tx\_hash  = double\_sha256 (transaction\_bytes )

print(f"Hash de la transacción:  {tx\_hash .hex()}")

![](data:image/png;base64...)

Algoritmo de consenso

Un algoritmo de consenso es un conjunto de reglas y mecanismos que permite a los

participantes de la red llegar a un acuerdo sobre la validez y el orden de las

transacciones. Estos algoritmos garantizan la seguridad, la integridad y la

descentralización de la red blockchain, y pueden variar en términos de requerimientos

computacionales, participación de los nodos y distribución de poder.

![](data:image/png;base64...)

Bitcoin: Algoritmo de consenso - PoW

PoW (Proof of Work):

En este algoritmo, los nodos compiten para resolver un desafío criptográﬁco

complejo, lo que requiere una gran cantidad de poder computacional. El primer nodo

en encontrar la solución correcta tiene derecho a agregar un nuevo bloque a la

cadena y recibir una recompensa. Este proceso se conoce como "minería" y ayuda a

garantizar la seguridad y la integridad de la red blockchain.

![](data:image/png;base64...)

Bitcoin: Algoritmo de consenso - PoW

PoW (Proof of Work):

Los mineros deben encontrar un valor de tal manera que el hash SHA-256 del

encabezado del bloque resulte en un número que esté por debajo de un objetivo

dado, conocido como "diﬁcultad".

Esta tarea requiere una gran cantidad de intentos y consume mucha energía, pero

una vez que se encuentra una solución, es fácil para otros nodos veriﬁcarla.

https://blockchain-academy.hs-mittweida.de/2021/05/proof-of-work-simulator/

![](data:image/png;base64...)

Bitcoin: Algoritmo de consenso - PoW

import hashlib

#ejemplo4.py

def proof\_of\_work(block\_data, difficulty="0000"):

max\_nonce = 10000000 # Ajustar para evitar bucles infinitos

target = int(difficulty + "F" \* (64 - len(difficulty)), 16)

for nonce in range(max\_nonce):

data = f"{block\_data}{nonce}".encode()

hash\_result  = hashlib.sha256(data).hexdigest()

if int(hash\_result, 16) < target:

return nonce, hash\_result

return None, None

# Datos del bloque

block\_data = "Información del bloque 12345"

nonce, hash\_result = proof\_of\_work(block\_data)

print(f"Nonce: {nonce}")

print(f"Hash: {hash\_result}")

![](data:image/png;base64...)

UTXO

![](data:image/png;base64...)

Bitcoin: Transacciones UTXO

UTXO:

Cuando se envía Bitcoin desde una wallet, los fondos no se transﬁeren en la misma

forma en que se moverían en una cuenta bancaria tradicional. En su lugar, se utilizan

las "salidas no gastadas" (UTXOs) de transacciones anteriores. Al realizar una nueva

transacción, el remitente selecciona una o más de estas UTXOs como entrada.

![](data:image/png;base64...)

Bitcoin: Transacciones UTXO

Cada transacción tiene al menos dos salidas:

● Dirección externa (receptor): Esta salida contiene los fondos que se envían al

destinatario. La cantidad exacta se deﬁne en la transacción.

● Dirección interna (cambio): Cualquier cantidad de Bitcoin que no se haya

transferido al destinatario (el cambio) se devuelve al remitente. Sin embargo, en

lugar de volver a la misma dirección, las wallets generan automáticamente una

nueva "dirección interna" para este propósito, lo que mejora la privacidad.

![](data:image/png;base64...)

Bitcoin: Transacciones UTXO

Implicaciones de privacidad

Al usar direcciones internas para el cambio, se evita que sea evidente qué parte de

una transacción corresponde al cambio y cuál al destinatario. Esto mejora la

privacidad de los usuarios, ya que reduce la posibilidad de rastrear movimientos

especíﬁcos de fondos.

![](data:image/png;base64...)

Bitcoin: Transacciones UTXO

Ejemplo:

● Si una wallet tiene 1 BTC disponible y se quiere enviar 0.6 BTC a un destinatario,

la transacción podría verse así:

○ Entrada: 1 BTC (proveniente de una UTXO anterior).

■ Salida 1 (receptor): 0.6 BTC enviado a la dirección del destinatario.

■ Salida 2 (cambio): 0.399 BTC (menos comisiones de minería) enviado

a una nueva dirección generada por la wallet del remitente.

![](data:image/png;base64...)

Bitcoin: Transacciones UTXO

https://mempool.space/es/tx/3fd926b2d5f03223311af35847cf5a7b8efb3285e1e9518a1e868ae57c

2ada0a

![](data:image/png;base64...)

Frase semilla

![](data:image/png;base64...)

Frase semilla

a menudo llamada "seed phrase", "recovery phrase" o "mnemonic phrase", es una

representación legible para el ser humano de una semilla que se utiliza para

generar deterministicamente un árbol de claves privadas. Esta frase semilla

suele consistir en una lista de palabras, generalmente entre 12 y 24, tomadas de

un diccionario especíﬁco.

La introducción de frases semilla surge del concepto de "carteras deterministas"

(deterministic wallets) o HD (Hierarchical Deterministic) wallets en el espacio de

criptomonedas. Una HD wallet permite generar un árbol inﬁnito de claves

privadas (y, por ende, públicas) a partir de una única semilla.

![](data:image/png;base64...)

Frase semilla(usabilidad)

Derivación de Claves: A partir de esta semilla, se puede generar deterministicamente una serie inﬁnita de claves

privadas. Estas claves se generan en una estructura jerárquica, lo que signiﬁca que puedes tener claves "hijas" derivadas

de claves "madres", y así sucesivamente.

Privacidad y Organización: Al utilizar HD wallets, se puede generar una nueva dirección de Bitcoin (o cualquier otra

criptomoneda) para cada transacción, lo que mejora la privacidad. A pesar de generar muchas direcciones, todas pueden

ser recuperadas a partir de la misma frase semilla.

Restauración: Si alguna vez se pierde el acceso a tu dispositivo o cartera, se puede usar la frase semilla para restaurar

los fondos en otro dispositivo o software compatible. Al ingresar la frase semilla, el nuevo software puede regenerar

todas tus claves privadas y, por ende, acceder a las direcciones y fondos asociados.

![](data:image/png;base64...)

Frase semilla

#ejemplo5.py

#pip install mnemonic

#pip install git+https://github.com/primal100/pybitcointools

from cryptos import entropy\_to\_words, Bitcoin

import os

words = entropy\_to\_words(os.urandom(16))

print("mi frase semilla:", words)

coin = Bitcoin()

wallet = coin.wallet(words)

print("path de derivación:", wallet.keystore.root\_derivation)

print("privada maestra:", wallet.keystore.xprv)

print("pública maestra:", wallet.keystore.xpub)

addr1 = wallet.new\_receiving\_address()# creando pública de recepción

print("addr1:", addr1)

print("privada de addr1:", wallet.privkey(addr1))

addr2 = wallet.new\_change\_address()# creando 2da pública de recepción

print("addr2:", addr2)

print("privada addr2:",wallet.privkey(addr2))

![](data:image/png;base64...)