![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

Clase 03

![](data:image/png;base64...)

Solidity

![](data:image/png;base64...)

Solidity

Es un lenguaje de programación de alto nivel compilado diseñado especíﬁcamente para escribir smart contracts en la

plataforma Ethereum. Fue propuesto por Gavin Wood en 2014 y desde entonces se ha convertido en el lenguaje de

programación principal para el desarrollo de smart contracts en Ethereum.

![](data:image/png;base64...)

Solidity: tipos de datos

❖ Primitivos:

➢  Booleanos: bool (con valores true o false).

➢ Enteros: int y uint (para números enteros con y sin signo, respectivamente). Ambos pueden tener tamaños

múltiples de 8 bits hasta 256 bits, como int8, int16... int256 y uint8, uint16... uint256.

❖ Direcciones:

➢  address: Representa una dirección Ethereum de 20 bytes.

➢ address payable: Similar a address, pero permite recibir y enviar ether.

❖ Bytes:

➢  bytes1, bytes2,..., bytes32 (secuencias de bytes de longitud ﬁja).

❖ Tipos de Punto Flotante:

➢  No hay soporte nativo para tipos de punto ﬂotante en Solidity debido a complicaciones con la precisión y la

determinística en la EVM.

![](data:image/png;base64...)

Solidity: tipos de datos

❖ Arrays:

➢ Arrays de longitud ﬁja y dinámica, por ejemplo, uint[5] (ﬁjo) y uint[] (dinámico).

❖ Bytes Dinámicos: bytes (similares a bytes[], pero de longitud dinámica).

❖ Strings: string (representa una cadena de caracteres UTF-8 de longitud dinámica).

❖ Maps: mapping(key => value). Funcionan como diccionarios o tablas hash, donde key puede ser casi cualquier

tipo excepto un mapping, y value puede ser cualquier tipo, incluido otro mapping.

❖ Structs: Deﬁnen estructuras personalizadas.

❖ Enums: Se utilizan para deﬁnir variables que pueden tener uno de los valores predeﬁnidos.

![](data:image/png;base64...)

Solidity: tipos de datos

![](data:image/png;base64...)

Solidity: tipos de datos

![](data:image/png;base64...)

Solidity: estructuras de control

![](data:image/png;base64...)

Solidity: estructuras de control

Hay que tener cuidado con los bucles en Solidity, ya que los bucles que consuman demasiado gas pueden resultar en

transacciones que no se puedan conﬁrmar debido a superar el límite de gas del

![](data:image/png;base64...)

Solidity: deﬁnición de un contrato

![](data:image/png;base64...)

Solidity: funciones de contrato

se pueden clasiﬁcar según su visibilidad y comportamiento.

➔ Funciones de Estado (State Functions): Estas son funciones que pueden modiﬁcar el estado del contrato (es

decir, cambiar el valor de una o más variables de estado). Estas funciones consumen gas cuando son llamadas y

las transacciones que las invocan deben ser validadas en un bloque.

➔ Funciones de Sólo Lectura (View Functions): Estas funciones no pueden modiﬁcar el estado del contrato y sólo

leen valores. Se pueden llamar externamente y no consumen gas cuando se invocan de esta manera (porque no

generan una transacción real en la cadena de bloques). Se declaran con el modiﬁcador view.

➔ Funciones Pura (Pure Functions): Son similares a las funciones view, pero son aún más restrictivas: no pueden

leer ni modiﬁcar el estado del contrato. Están diseñadas para retornar un valor basado únicamente en sus

argumentos. Se declaran con el modiﬁcador pure.

![](data:image/png;base64...)

Solidity: funciones de contrato cont…

➔ Funciones de Pago (Payable Functions): Son funciones que pueden recibir Ether. Si envías Ether a una función

que no está marcada con el modiﬁcador payable, la transacción fallará. Las funciones payable son esenciales

para contratos que deben manejar Ether directamente, como un contrato de crowdfunding.

➔ Funciones Internas (Internal Functions): Estas funciones sólo pueden ser llamadas desde el propio contrato o

desde contratos derivados. No pueden ser llamadas directamente por transacciones externas. Son útiles para

dividir la lógica del contrato en partes más pequeñas, para reutilizar código, o para implementar detalles de bajo

nivel que no deberían ser expuestos a los usuarios del contrato.

➔ Funciones Externas (External Functions): Estas funciones están destinadas a ser llamadas desde transacciones

externas y no desde otras funciones dentro del contrato. En algunos casos, pueden ser más eﬁcientes en

términos de gas cuando se llaman desde el exterior en comparación con las funciones public.

![](data:image/png;base64...)

Solidity: funciones de contrato cont II

➔ Funciones Fallback y Receive:

◆ Fallback: Antes de la versión 0.6.0 de Solidity, si un contrato recibía Ether sin que ninguna función fuese

llamada (es decir, una transacción de Ether a la dirección del contrato sin datos adicionales), y si el contrato

no tenía una función marcada como payable, entonces la función fallback se ejecutaba. Esta función no

puede tener argumentos ni retornar nada.

◆ Receive: Introducido en la versión 0.6.0, es una variante especializada de la función fallback que sólo se

ejecuta cuando no se llama a ninguna otra función y no se proporcionan datos.

La visibilidad de las funciones (y también de las variables de estado) en Solidity se deﬁne mediante los modiﬁcadores

public, private, internal y external.

![](data:image/png;base64...)

Solidity: funciones de contrato cont III

![](data:image/png;base64...)

Solidity: modiﬁcadores

Los modiﬁcadores en Solidity son herramientas que se utilizan para cambiar el comportamiento de funciones o para

veriﬁcar ciertas condiciones antes de que una función sea ejecutada. En esencia, permiten añadir una lógica adicional a

la ejecución de una función de forma reutilizable y legible. Es común utilizarlos para veriﬁcar permisos, restricciones o

estados especíﬁcos del contrato.

● Deﬁnición: Un modiﬁcador se deﬁne de manera similar a una función, pero con la palabra clave modiﬁer en lugar

de function.

● Uso del placeholder \_: Dentro del cuerpo del modiﬁcador, el placeholder \_ se utiliza para indicar dónde debe

insertarse el código de la función que se modiﬁca. El código antes del \_ se ejecuta antes de la función, y el código

después del \_ se ejecuta después de la función (si lo hay).

● Aplicación a funciones: Una vez deﬁnido, el modiﬁcador puede ser añadido a una función añadiendo su nombre

después de la declaración de la función, antes del {.

![](data:image/png;base64...)

Solidity: modiﬁcadores cont …

![](data:image/png;base64...)

Solidity: import y herencia

En Solidity, la directiva import se utiliza para incluir código de otros archivos. Esto es especialmente útil para la

organización de código y para reutilizar bibliotecas o contratos existentes.

Deﬁnición Básica de Herencia:

Un contrato puede heredar de uno o más contratos usando la palabra clave is.

![](data:image/png;base64...)

Solidity: import y herencia

Orden de Herencia:

Cuando un contrato hereda de múltiples contratos, el orden en el que se enumeran es importante porque determina el

orden de inicialización y el orden de disposición del almacenamiento.

![](data:image/png;base64...)

Solidity: import y herencia

Sobrescritura:

Las funciones, las variables de estado y los modiﬁcadores en los contratos derivados pueden sobrescribir las

deﬁniciones de los contratos base.

![](data:image/png;base64...)

Solidity: import y herencia

Super:Si un contrato deriva de múltiples contratos y varios de ellos deﬁnen una función (o un modiﬁcador) con el mismo

nombre, super se utiliza para acceder a la función o modiﬁcador de la siguiente base en la cadena de herencia.

![](data:image/png;base64...)

Solidity: import y herencia

Constructores y Herencia:Si un contrato base tiene un constructor, este debe ser llamado en el constructor del contrato

derivado. Si el contrato base tiene un constructor sin argumentos, este se llamará automáticamente.

![](data:image/png;base64...)

Solidity: herencia e interfaces

Interfaces y Herencia:

Además de heredar de otros contratos, un contrato también puede heredar de interfaces, que son como contratos pero

no pueden tener implementaciones de funciones ni variables de estado.

![](data:image/png;base64...)

Solidity: Modiﬁcadores de Tipo de Datos

➢ memory: Indica que la variable se almacena temporalmente y desaparecerá entre llamadas de función externa.

➢ storage: Indica que la variable se almacena de forma persistente en el almacenamiento del contrato.

➢ calldata: Es similar a memory, pero es inmutable y se utiliza principalmente para parámetros de funciones

externas.

➢ constant / immutable:Estos modiﬁcadores se utilizan para variables de estado que no cambiarán después de que

se asignen. Mientras que constant se usaba para variables cuyo valor se conoce en tiempo de compilación,

immutable es para variables que se asignan una vez durante la construcción y no cambian después.

![](data:image/png;base64...)

Solidity: Modiﬁcadores de Tipo de Datos

![](data:image/png;base64...)

Solidity: palabras clave o reservadas

Algunas importantes, aparte de las ya vistas:

`abstract`: Indica que un contrato no puede ser desplegado por sí mismo y debe ser heredado por otro contrato.

`delete`: Usado para borrar contenido en storage o para resetear una variable a su valor predeterminado.

`library`: Deﬁne una biblioteca, que es similar a un contrato pero no tiene variables de estado.

`override`: Indica que una función sobrescribe una función heredada.

`this`: Reﬁere a la instancia actual del contrato.

`try-catch`: Utilizado para manejar fallos en llamadas externas.

`type`: Obtiene el tipo de una variable.

`using`: Indica que un contrato usa una biblioteca especíﬁca.

![](data:image/png;base64...)

Solidity: Eventos

Un evento es una característica que permite a los contratos inteligentes emitir registros que las dapps front-end o las

aplicaciones externas pueden "escuchar" y reaccionar en consecuencia. Estos registros se almacenan en los logs de la

blockchain, lo que signiﬁca que son menos costosos en términos de gas en comparación con el almacenamiento de

datos en el propio contrato.

En este ejemplo, cada vez que se llama a la función setData, se emite el evento DataChanged registrando quién cambió los datos, el valor anterior

y el valor nuevo. La palabra indexed en el evento signiﬁca que ese argumento se puede usar como un ﬁltro para buscar o escuchar eventos

especíﬁcos.

![](data:image/png;base64...)

Links

➔ remix: http://remix.ethereum.org/

➔ faucet:

https://cloud.google.com/application/web3/faucet/ethereum/sepoli

a

➔ metamask: chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome

➔ explorador de bloques

➔ validar un contrato

![](data:image/png;base64...)